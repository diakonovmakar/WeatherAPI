from django.http import JsonResponse

from weather.services import weather_status, get_weather, assign_parameters


def index(request):
    params = assign_parameters(request)
    if len(params) < 3:
        error = params
        return JsonResponse(error)
    weather = get_weather(params)
    print(weather)
    for i in weather:
        print(len(i))
        if len(i) == 5:
            error = weather
            return JsonResponse(error)
    result = weather_status(weather)
    return JsonResponse(result)
