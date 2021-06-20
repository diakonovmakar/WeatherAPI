from weather.services import validate_country_code, validate_date, weather_status, get_weather
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays a forecast depending on a date and a country code.'

    def add_arguments(self, parser):
        parser.add_argument('date', type=str, help='Date for a forecast (YYYY-MM-DD)')
        parser.add_argument('country_code', type=str, help='Country code for a forecast')

    def handle(self, *args, **kwargs):
        country_code = kwargs['country_code']
        date = kwargs['date']
        code_validation = validate_country_code(country_code)
        date_validation = validate_date(date)
        if code_validation['success'] is True and date_validation['success'] is True:
            weather = get_weather(date, country_code)
            result = weather_status(weather)
            return self.stdout.write("%s" % result)
        elif code_validation['success'] is not True:
            return self.stdout.write("%s" % code_validation)
        elif date_validation['success'] is not True:
            return self.stdout.write("%s" % date_validation)
        else:
            return self.stdout.write({'error': 'Unexpected error.'})
