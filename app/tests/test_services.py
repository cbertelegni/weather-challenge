import pytest
from app.services import WeatherService
from app.clients import WeatherClient
from app.tests.base_tests import BaseTestSetUp
from app.schemas import TemperatureUnitsEnum

class TestWeatherService(BaseTestSetUp):

    def test_builder(self):
        weather_service = WeatherService.build()
        assert isinstance(weather_service, WeatherService)
        assert isinstance(weather_service.client, WeatherClient)

    @pytest.mark.parametrize("expected_key", [
        ('country'),
        ('city'),
        ('description'),
        ('sunrise'),
        ('sunset'),
        ('temp'),
        ('feels_like'),
        ('temp_min'),
        ('temp_max'),
        ('pressure'),
        ('humidity'),
        ('visibility'),
        ('geo_coordinates'),
        ('wind')
    ])
    def test_get_weather_return_expected_key(self, expected_key, mock_client_response_ok):
        weather_service = WeatherService.build()
        response = weather_service.get_weather(
            country=self.country,
            city=self.city,
            units=TemperatureUnitsEnum.imperial
        )
        assert expected_key in response
