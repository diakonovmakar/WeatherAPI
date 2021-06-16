from django.http import JsonResponse

from weather.services import runner, weather_status, what_weather


def index(request):
    weather = runner(request)
    result = weather_status(weather)
    return JsonResponse(result)
