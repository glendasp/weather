from pyowm import OWM
from lib import Ziptastic

__all__ = ['get_city_state', 'current_temperature']

# https://home.openweathermap.org/users/sign_up
OWM_API_KEY = ''
# Ziptastic seems to work with an empty API...
ZIPTASTIC_API_KEY = ''


def get_city_state(zip_code):
    ziptastic = Ziptastic(ZIPTASTIC_API_KEY)
    location = ziptastic.get_from_postal_code(zip_code)
    return location['city'], location['state']


def current_temperature(location, unit='fahrenheit'):
    """Return the current temperature at a location (City,State)."""

    owm = OWM(OWM_API_KEY)
    observation = owm.weather_at_place(location)
    weather = observation.get_weather()
    temperature_info = weather.get_temperature(unit)
    temperature = temperature_info.get('temp')

    return temperature
