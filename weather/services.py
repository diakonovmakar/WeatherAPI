import requests as rq


def what_weather(request):
    date = request.GET.get('date', '')
    country_code = request.GET.get('country_code', '')

    base_url = 'http://api.weatherapi.com/v1/forecast.json'

    if country_code == 'CZ':
        coordinates = '50.073658, 14.418540'  # Prague, CZ
    elif country_code == 'UK':
        coordinates = '51.509865, -0.118092'  # London, UK
    elif country_code == 'SK':
        coordinates = '48.148598, 17.107748'  # Bratislava, SK

    url_params = {
        'key': '3a01053352db4121b28133514211506',
        'q': coordinates,  
        'dt': date,
    }

    country_weather = rq.get(base_url, params=url_params).json()

    weather = {
        'country': country_weather['location']['country'],
        'date': country_weather['forecast']['forecastday'][0]['date'],
        'temperature': country_weather['forecast']['forecastday'][0]['day']['avgtemp_c']
    }
    return weather


def weather_status(weather):
    if weather['temperature'] > 20:
        status = {'forecast': 'good'}
    elif weather['temperature'] <= 20 and weather['temperature'] >= 10:
        status = {'forecast': 'soso'}
    else:
        status = {'forecast': 'bad'}
    return status

