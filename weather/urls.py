from django.urls import path
from .views import ForecastWeatherView

#  app_name = 'weather'
urlpatterns = [
    path('', ForecastWeatherView.as_view()),
]
