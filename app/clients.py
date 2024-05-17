from urllib.parse import urljoin
import requests
from fastapi import status
from requests import Response
from app.core import settings
from app.schemas import TemperatureUnitsEnum
from app.exceptions import (
    WeatherClientException,
    CityNotFoundException
)

class BaseClient:
    def __init__(self, client_url: str = settings.WEATHER_API_BASE_URL) -> None:
        self.client_url = client_url

    def get(self, method: str, params: dict = {}) -> Response:
        url = urljoin(self.client_url, method)
        response = requests.get(url, params=params)
        return response


class WeatherClient(BaseClient):
    def __init__(
            self,
            client_url: str = settings.WEATHER_API_BASE_URL,
            api_key: str = settings.WEATHER_API_KEY
    ) -> None:
        super().__init__(client_url)
        self.api_key = api_key

    def _get_params(self, **kwargs):
        params = {
            'appid': self.api_key
        }
        params.update(kwargs)
        return params

    def fetch_weather(self, country: str, city: str, units: TemperatureUnitsEnum):
        params = self._get_params(
            q=f'{city},{country}',
            units=units
        )
        response = self.get(method='data/2.5/weather', params=params)
        try:
            response.raise_for_status()
        except Exception:
            if response.status_code == status.HTTP_404_NOT_FOUND:
                raise CityNotFoundException
            else:
                raise WeatherClientException
        else:
            return response.json()
