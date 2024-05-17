from fastapi import status
from app.tests.base_tests import BaseTestSetUp
from app.services import WeatherService
from app.schemas import WeatherSchema
from app.schemas import TemperatureUnitsEnum


class TestApiWeather(BaseTestSetUp):
    api_method = '/weather'

    def test_200_ok(self, test_client, mock_client_response_ok):
        response = test_client.get(
            self.api_method,
            params={
                "city": self.city,
                "country": self.country,
                "units": TemperatureUnitsEnum.imperial.value
            }
        )
        assert response.status_code == status.HTTP_200_OK

        weather_service = WeatherService.build()
        weather = weather_service.get_weather(
            country=self.country, city=self.city, units=TemperatureUnitsEnum.imperial
        )
        assert response.json() == WeatherSchema(**weather).model_dump()

    def test_must_raise_404_when_client_raise_404(self, test_client, mock_client_response_404):
        response = test_client.get(
            self.api_method,
            params={
                "city": self.city,
                "country": self.country,
                "units":TemperatureUnitsEnum.imperial.value
            }
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_must_raise_500_when_client_raise_error(self, test_client, mock_client_response_500):
        response = test_client.get(
            self.api_method,
            params={
                "city": self.city,
                "country": self.country,
                "units":TemperatureUnitsEnum.imperial.value
            }
        )
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR