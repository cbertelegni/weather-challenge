from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, Request, status, HTTPException
from app.core import settings
from fastapi_cache.decorator import cache
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from app.schemas import WeatherSchema, TemperatureUnitsEnum
from app.services import WeatherService
from app.exceptions import WeatherClientException, CityNotFoundException


CACHE_MAX_AGE = 120


@asynccontextmanager
async def lifespan(app: FastAPI):
    FastAPICache.init(InMemoryBackend())
    yield


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)



@app.exception_handler(CityNotFoundException)
def city_not_found_exception_handler(request: Request, exc: CityNotFoundException):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.exception_handler(WeatherClientException)
def city_not_found_exception_handler(request: Request, exc: WeatherClientException):
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get("/weather")
@cache(expire=CACHE_MAX_AGE)
def get_weather(
    city: str,
    country: str,
    units: TemperatureUnitsEnum = TemperatureUnitsEnum.imperial,
    weather_service: WeatherService = Depends(WeatherService.build)
) -> WeatherSchema:
    return weather_service.get_weather(
        city=city,
        country=country,
        units=units
    )