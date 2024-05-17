import pytest
import responses
from responses import matchers
from urllib.parse import urljoin
from fastapi import status
from app.core import settings
from app.schemas import TemperatureUnitsEnum

class BaseTestSetUp:
    @classmethod
    def setup_class(cls):
        cls.city = 'Córdoba'
        cls.country = 'AR'
        cls.client_url = urljoin(settings.WEATHER_API_BASE_URL, 'data/2.5/weather')
        cls.params = {
            'q': f'{cls.city},{cls.country}',
            'appid': settings.WEATHER_API_KEY,
            'units': TemperatureUnitsEnum.imperial
        }
        cls.client_response = {
            "coord": {
                "lon": -64.1811,
                "lat": -31.4135
            },
            "weather": [
                {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01n"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 283.57,
                "feels_like": 282.39,
                "temp_min": 281.62,
                "temp_max": 283.57,
                "pressure": 968,
                "humidity": 66
            },
            "visibility": 10000,
            "wind": {
                "speed": 2.06,
                "deg": 310
            },
            "clouds": {
                "all": 0
            },
            "dt": 1715907615,
            "sys": {
                "type": 2,
                "id": 2036678,
                "country": "AR",
                "sunrise": 1715857094,
                "sunset": 1715894891
            },
            "timezone": -10800,
            "id": 3860259,
            "name": "Córdoba",
            "cod": 200
            }

    @pytest.fixture(scope='function')
    def mock_client_response_ok(self, mocked_responses):
        mocked_responses.add(
            responses.GET,
            self.client_url,
            match=[
                matchers.query_param_matcher(self.params)
            ],
            json=self.client_response,
            status=status.HTTP_200_OK
        )
        yield mocked_responses

    @pytest.fixture(scope='function')
    def mock_client_response_404(self, mocked_responses):
        mocked_responses.add(
            responses.GET,
            self.client_url,
            match=[
                matchers.query_param_matcher(self.params)
            ],
            status=status.HTTP_404_NOT_FOUND
        )
        yield mocked_responses

    @pytest.fixture(scope='function')
    def mock_client_response_401(self, mocked_responses):
        mocked_responses.add(
            responses.GET,
            self.client_url,
            match=[
                matchers.query_param_matcher(self.params)
            ],
            status=status.HTTP_401_UNAUTHORIZED
        )
        yield mocked_responses

    @pytest.fixture(scope='function')
    def mock_client_response_500(self, mocked_responses):
        mocked_responses.add(
            responses.GET,
            self.client_url,
            match=[
                matchers.query_param_matcher(self.params)
            ],
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        yield mocked_responses
