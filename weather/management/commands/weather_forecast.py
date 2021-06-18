from weather.services import assign_parameters, weather_status, get_weather
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays a forecast depending on a date and a country code.'

    def add_arguments(self, parser):
        parser.add_argument('date', type=str, help='Date for a forecast (YYYY-MM-DD)')
        parser.add_argument('country_code', type=str, help='Country code for a forecast')

    def handle(self, *args, **kwargs):
        url_params = {
        'key': '3a01053352db4121b28133514211506',
        'q': '',
        'dt': '',
        }
        coordinates = {
        'CZ': '50.073658, 14.418540',  #  Prague
        'SK': '48.148598, 17.107748',  #  Bratislava
        'UK': '51.509865, -0.118092',  #  London
        }
        url_params['dt'] = kwargs['date']
        url_params['q'] = coordinates[f'{kwargs["country_code"]}']
        weather = get_weather(url_params)
        result = weather_status(weather)
        self.stdout.write("%s" % result)
