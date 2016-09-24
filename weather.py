import sys
import click

from api.dummy import DummyAPI


@click.command()
@click.argument('zip_code')
def main(zip_code):
    """Displays the current temperature for the specified zip code."""
    
    current_temp = DummyAPI().current_temp(zip_code)

    if current_temp is None:
        click.echo('No information found for {}'.format(zip_code))
        sys.exit()

    click.echo('It is currently {} in {}'.format(current_temp, zip_code))


if __name__ == '__main__':
    main()
