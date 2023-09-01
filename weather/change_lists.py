"""The module contains ChangeLists of weather app."""

import json
from urllib.parse import urljoin

import requests
from django.conf import settings
from django.contrib.admin.views.main import ChangeList

from weather.models import ForecastDay

DEFAULT_LIST_PER_PAGE = 25


class ForecastDayChangeList(ChangeList):
    """Overrides the list of ForecastDay objects in the admin panel."""

    def __init__(self, *args, **kwargs):
        self.has_next = False
        self.result_list = []
        self.result_count = 0
        self.show_admin_actions = False

        super().__init__(*args, **kwargs)

        self.list_per_page = DEFAULT_LIST_PER_PAGE

    @staticmethod
    def _fetch_forecasts():
        """Sends a request to receive a weather forecast."""

        params = {
            'q': settings.WEATHER_API_CITY,
            'days': settings.WEATHER_API_DAYS,
            'key': settings.WEATHER_API_KEY,
        }
        try:
            remote_forecasts = requests.get(
                urljoin(settings.WEATHER_API_URL, 'forecast.json'),
                params=params,
            )
            remote_forecasts.raise_for_status()
            remote_forecasts = remote_forecasts.json()
            remote_forecasts = remote_forecasts['forecast']['forecastday']
        except (KeyError, json.JSONDecodeError, requests.RequestException):
            remote_forecasts = []

        return remote_forecasts

    def get_results(self, request):
        """Returns a list of objects to display in admin panel."""

        super().get_results(request)

        remote_forecasts = self._fetch_forecasts()
        forecasts = []
        for index, remote_forecast in enumerate(remote_forecasts):
            forecast = ForecastDay()
            forecast.id = index
            forecast.created_at = remote_forecast['date']
            forecast.max_temp = remote_forecast['day']['maxtemp_c']
            forecast.avg_temp = remote_forecast['day']['avgtemp_c']
            forecast.max_wind = remote_forecast['day']['maxwind_kph']
            forecast.avg_humidity = remote_forecast['day']['avghumidity']
            forecast.condition = remote_forecast['day']['condition']['text']

            forecasts.append(forecast)

        self.result_list = forecasts
        self.result_count = len(forecasts)

    def url_for_result(self, result):
        """We haven't implemented object view."""

        return ''
