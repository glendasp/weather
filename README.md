# weather
A command-line program written in Python to display information about the weather.

## Installation

### Download and Install
You will probably want to do this inside a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

```
pip install git+git://github.com/masonelmore/weather.git
```

### API key
Sign up for an account at [OpenWeatherMap](http://openweathermap.org/) to get an API key.  weather will look for your key in these locations: 
* the `--api-key` command line option
* an environment variable named `OWM_API_KEY`
* a "configuration" file
  * Windows: `%LocalAppData%\weather-py\owm_key`
  * Linux/Mac: `~/.config/weather-py/owm_key`

## Usage
```
$ weather 30359
Current weather for Atlanta, GA
Temperature: 19 °C
Status: Clear
```
