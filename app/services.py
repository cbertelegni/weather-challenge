from typing import Any
from app.schemas import WeatherSchema
from app.clients import WeatherClient
from fastapi import Depends


class WeatherService:
    def __init__(self, client: WeatherClient) -> None:
        self.client = client

    @classmethod
    def build(cls):
        client = WeatherClient()
        return cls(client=client)

    def transform_weather_response(self, weather_response: dict):
        weather = {
            'city': weather_response['name'],
            'visibility': weather_response['visibility'],
            'description': weather_response['weather'][0]['description'], # I assumed that this value will be always present
            'wind': weather_response['wind'],
            'geo_coordinates': weather_response['coord'],
            'wind': weather_response['wind'],
        }
        weather.update(weather_response['main'])
        weather.update(weather_response['sys'])
        return weather

    def get_weather(self, country: str, city: str, units: str) -> WeatherSchema:
        weather_response = self.client.fetch_weather(country=country, city=city, units=units)
        weather = self.transform_weather_response(weather_response=weather_response)
        return weather
