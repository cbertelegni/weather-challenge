from pydantic import BaseModel
from enum import Enum



class TemperatureUnitsEnum(str, Enum):
    imperial = "imperial"  # Fahrenheit
    metric = "metric"  # Celsius

class CoordinateSchema(BaseModel):
    lat: float
    lon: float


class WindSchema(BaseModel):
    speed: float
    deg: int


class WeatherSchema(BaseModel):
    country: str
    city: str
    description: str
    sunrise: int
    sunset: int
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    visibility: int
    geo_coordinates: CoordinateSchema
    wind: WindSchema
