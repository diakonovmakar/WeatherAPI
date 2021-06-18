import requests as rq
import datetime as dt


def assign_parameters(request):
    url_params = {
        'key': '3a01053352db4121b28133514211506',
        'q': '',
        'dt': '', }
    coordinates = {
    'CZ': '50.073658, 14.418540',  #  Prague
    'SK': '48.148598, 17.107748',  #  Bratislava
    'UK': '51.509865, -0.118092'}  #  London    

    dates_db = create_dates_db()
    if request.GET.get('date', '') not in dates_db:
        return {'Error': 'The date is incorrect'}
    elif request.GET.get('country_code', '') not in coordinates.keys():
        return {'Error': 'The country code is incorrect'}
    else:
        url_params['dt'] = request.GET.get('date', '')
        url_params['q'] = coordinates[f'{request.GET.get("country_code", "")}']
        return url_params


def create_dates_db():
    dates_db = {}
    today = dt.datetime.now().date()
    for i in range(0, 16, 1):
        dates_db[f'{today + dt.timedelta(days=i)}'] = today + dt.timedelta(days=i)
    return dates_db


def get_weather(url_params):
    base_url = 'http://api.weatherapi.com/v1/forecast.json'
    try:
        response = rq.get(base_url, params=url_params)
    except rq.ConnectionError:
        return {'Error': 'Network error'}

    if response.status_code == 200:
        return {
#        'country': country_weather['location']['country'],
#        'date': country_weather['forecast']['forecastday'][0]['date'],
        'temperature': response.json()['forecast']['forecastday'][0]['day']['avgtemp_c']
        }
    else:
        return {'Error': 'Forcast server do not avaiable. Try again later'}


def weather_status(weather):
    if weather['temperature'] > 20:
        return {'forecast': 'good'}
    elif weather['temperature'] <= 20 and weather['temperature'] >= 10:
        return {'forecast': 'soso'}
    else:
        return {'forecast': 'bad'}
