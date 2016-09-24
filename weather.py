import click
from external_api import *


@click.command()
@click.argument('zip_code')
def main(zip_code):
    """Displays the current temperature for the specified zip code."""
    city, state = get_city_state(zip_code)
    click.echo('Fetching temperature for {}, {}'.format(city, state))

    temperature = current_temperature('{},{}'.format(city, state))
    click.echo('It is currently {}F'.format(temperature))


if __name__ == '__main__':
    main()
