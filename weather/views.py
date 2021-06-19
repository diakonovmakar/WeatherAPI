from django.http import JsonResponse
from django.views import View

from weather.services import weather_status, get_weather, validate_date, validate_country_code


class ForecastWeather(View):
    def get(self, request):
        date = request.GET.get('date', '')
        country_code = request.GET.get('country_code', '')

        code_validation = validate_country_code(country_code)
        date_validation = validate_date(date)
        print(date, country_code)
        if code_validation['success'] is True and date_validation['success'] is True:
            weather = get_weather(date, country_code)
            result = weather_status(weather)
            return JsonResponse(result, status=200)
        elif code_validation['success'] is not True:
            print(code_validation)
            return JsonResponse(code_validation, status=400)
        elif date_validation['success'] is not True:
            print(date_validation)
            return JsonResponse(date_validation, status=400)
        else:
            return JsonResponse({'error': 'Unexpected error.'}, status=500)
