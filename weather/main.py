import sys
import click
from pyowm import OWM
from pyowm.exceptions.api_call_error import APICallError
from weather.lib import Ziptastic
from weather import api_keys


class PostalCodeNotFound(Exception):
    """Raised when an invalid postal code is passed to the program."""


@click.command()
@click.option('--units', type=click.Choice(['celsius', 'fahrenheit']),
              default='celsius')
@click.option('--api-key', help='API key for OpenWeatherMap')
@click.argument('location')
def main(location, units, api_key):
    """Display the current weather forecast for a location.  Accepted formats
    for the location are: US postal code."""

    if api_key is not None:
        api_keys.set_key(api_key)

    try:
        city, state = get_city_state(location)
    except PostalCodeNotFound:
        click.echo('Error: "{}" is not a valid US postal code'.format(location))
        sys.exit()

    try:
        weather = get_weather(city, state)
    except APICallError:
        click.echo('An error occurred while connecting to OpenWeather Map.  '
                   'Make sure your API key is valid.')
        sys.exit()

    temperature_info = weather.get_temperature(units)
    # Display either C or F depending on the units.
    symbol = units[:1].upper()
    temperature = '{} °{}'.format(int(temperature_info['temp']), symbol)
    status = weather.get_status()

    click.echo('Current weather for {}, {}'.format(city, state))
    click.echo('Temperature: {}'.format(temperature))
    click.echo('Status: {}'.format(status))


def get_city_state(postal_code):
    """Return the city and state from a US postal code."""

    api = Ziptastic('')
    location = api.get_from_postal_code(postal_code)

    if location.get('message', None) == 'Not Found':
        raise PostalCodeNotFound

    city, state = location['city'], location['state']

    return city, state


def get_weather(city, state):
    """Return the weather at the city, state."""

    # OWM expects the place to be in the format of CITY,COUNTRY (Minneapolis,
    #  US).  The only problem with that is some cities like Bloomington are
    # ambiguous.  Querying the API with CITY,STATE (Minneapolis,Minnesota)
    # seems to work.  I don't think there are any two-character state codes
    # that clash with any countries.  We should probably expect bug reports,
    # though.
    api = OWM(api_keys.OWM)
    place = '{},{}'.format(city, state)
    observation = api.weather_at_place(place)
    weather = observation.get_weather()

    return weather


if __name__ == '__main__':
    main()
