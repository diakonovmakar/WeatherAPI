from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View

from weather.services import weather_status, get_weather, validate_date, validate_country_code

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@method_decorator(cache_page(CACHE_TTL), name='get')
class ForecastWeather(View):
    def get(self, request):
        date = request.GET.get('date', '')
        country_code = request.GET.get('country_code', '')

        code_validation = validate_country_code(country_code)
        date_validation = validate_date(date)

        if code_validation.success is True and date_validation.success is True:
            forecast = get_weather(date, country_code)

            if forecast.success is True:
                result = {'forecast': forecast.forecast}
                return JsonResponse(result, status=200)
            else:
                result = {'error': forecast.error}
                return JsonResponse(result, status=400)

        elif code_validation.success is not True:
            result = {'error': code_validation.error}
            return JsonResponse(result, status=400)

        elif date_validation.success is not True:
            result = {'error': date_validation.error}
            return JsonResponse(result, status=406)

        else:
            return JsonResponse({'error': 'Unexpected error'}, status=500)
