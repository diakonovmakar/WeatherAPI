from weather.services import weather_status, what_weather
from django.http import JsonResponse

# Create your views here.


def index(request):
    weather = what_weather(request)
    result = weather_status(weather)
    return JsonResponse(result)
