import pytest
from app.clients import WeatherClient
from app.tests.base_tests import BaseTestSetUp
from app.schemas import TemperatureUnitsEnum
from app.exceptions import (
    WeatherClientException,
    CityNotFoundException
)

class TestWeatherClient(BaseTestSetUp):
    
    def test_fetch_weather_response_ok(self, mock_client_response_ok):
        client = WeatherClient()
        response = client.fetch_weather(
            country=self.country, city=self.city, units=TemperatureUnitsEnum.imperial
        )
        assert response == self.client_response
    
    def test_raise_place_not_found_exc_if_404(self, mock_client_response_404):
        client = WeatherClient()
        with pytest.raises(CityNotFoundException):
            client.fetch_weather(
                country=self.country, city=self.city, units=TemperatureUnitsEnum.imperial
            )

    def test_raise_not_autoraized_api_key(self, mock_client_response_401):
        client = WeatherClient()
        with pytest.raises(WeatherClientException):
            client.fetch_weather(
                country=self.country, city=self.city, units=TemperatureUnitsEnum.imperial
            )

    def test_raise_internal_server_error(self, mock_client_response_500):
        client = WeatherClient()
        with pytest.raises(WeatherClientException):
            client.fetch_weather(
                country=self.country, city=self.city, units=TemperatureUnitsEnum.imperial
            )