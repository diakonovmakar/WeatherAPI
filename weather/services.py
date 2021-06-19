from django.http import JsonResponse
import requests as rq
import datetime as dt

coordinates = {
    'CZ': '50.073658, 14.418540',  #  Prague
    'SK': '48.148598, 17.107748',  #  Bratislava
    'UK': '51.509865, -0.118092'}  #  London


def get_weather(date, country_code):
    base_url = 'http://api.weatherapi.com/v1/forecast.json'
    url_params = {
        'key': '3a01053352db4121b28133514211506',
        'q': coordinates[country_code],
        'dt': date}
    try:
        response = rq.get(base_url, params=url_params)
    except rq.Connectionerror:
        return {
            'success': False,
            'error': 'Network error'}

    if response.status_code == 200:
        return {
            'temperature': response.json()['forecast']['forecastday'][0]['day']['avgtemp_c']}
    else:
        return {
            'success': False,
            'error': 'Forcast server unavaiable. Try again later'}


def validate_date(request_date):
    today = dt.datetime.now().date()
    max_date = today + dt.timedelta(days=15)
    try:
        date = dt.datetime.strptime(request_date, '%Y-%m-%d').date()
        if date >= today and date <= max_date:
            return {
                'success': True,
                'error': ''}
        else:
            return {
                'success': False,
                'error': 'The date is incorrect'}
    except ValueError:
        return {
            'success': False,
            'error': 'Date is not acceptable'}
    except:
        return {
        'success': False,
        'error': 'Unexpected error with a date'}


def validate_country_code(country_code):
    if country_code not in coordinates.keys():
        return {
            'success': False,
            'error': 'The country code is incorrect'}
    else:
        return {
            'success': True,
            'error': ''}


def weather_status(weather):
    if weather['temperature'] > 20:
        return {'forecast': 'good'}
    elif weather['temperature'] <= 20 and weather['temperature'] >= 10:
        return {'forecast': 'soso'}
    else:
        return {'forecast': 'bad'}
