from weather.services import weather_status, what_country, what_weather
from django.core.management.base import BaseCommand
from ...models import url_params


class Command(BaseCommand):
    help = 'Displays a forecast depending on a date and a country code.'

    def add_arguments(self, parser):
        parser.add_argument('date', type=str, help='Date for a forecast (YYYY-MM-DD)')
        parser.add_argument('country_code', type=str, help='Country code for a forecast')

    def handle(self, *args, **kwargs):
        date = kwargs['date']
        country_code = kwargs['country_code']
        url_params['dt'] = date
        what_country(country_code)
        weather = what_weather()
        result = weather_status(weather)
        self.stdout.write("%s" % result)
