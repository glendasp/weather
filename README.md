# weather
A command-line program written in Python to display information about the weather.

# Usage
This program uses APIs from [OpenWeatherMap](http://openweathermap.org/) and [Ziptastic](https://www.getziptastic.com/).  You can get the required API keys by signing up on their websites.  Ziptastic seems to not require an API key for their free service, so creating an account with them is optional.

Put your API keys in the `external_api.py` file:
```
OWM_API_KEY = 'YOUR KEY HERE'
ZIPTASTIC_API_KEY = 'YOUR KEY HERE (optional)'
```

Run the program with a US zip code:
```
$ python weather.py 30359
Fetching temperature for Atlanta, Georgia
It is currently 79.21F
```
