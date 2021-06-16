import requests as rq

from .models import url_params, coordinates


def what_weather():
    base_url = 'http://api.weatherapi.com/v1/forecast.json'
    country_weather = rq.get(base_url, params=url_params).json()

    return {
#        'country': country_weather['location']['country'],
#        'date': country_weather['forecast']['forecastday'][0]['date'],
        'temperature': country_weather['forecast']['forecastday'][0]['day']['avgtemp_c']
    }


def take_parameters(request):
    url_params['dt'] = request.GET.get('date', '')
    return request.GET.get('country_code', '')



def what_country(country_code):
    if country_code == 'CZ':
        url_params['q'] = coordinates['Prague']
    elif country_code == 'UK':
        url_params['q'] = coordinates['London']
    elif country_code == 'SK':
        url_params['q'] = coordinates['Bratislava']


def weather_status(weather):
    if weather['temperature'] > 20:
        return {'forecast': 'good'}
    elif weather['temperature'] <= 20 and weather['temperature'] >= 10:
        return {'forecast': 'soso'}
    else:
        return {'forecast': 'bad'}


def runner(request):
    country_code = take_parameters(request)
    what_country(country_code)
    return what_weather()
