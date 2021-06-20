from django.urls import path
from .views import ForecastWeather

#  app_name = 'weather'
urlpatterns = [
    path('', ForecastWeather.as_view()),
]
