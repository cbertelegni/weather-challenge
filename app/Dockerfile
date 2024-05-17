FROM python:3.10-alpine as weather_challenge_base

WORKDIR /src

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
RUN rm /src/requirements.txt

COPY . /src/app

# For Develoment
FROM weather_challenge_base as weather_challenge_dev

COPY requirements-dev.txt /src/requirements-dev.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements-dev.txt
RUN rm /src/requirements-dev.txt


EXPOSE 8000
EXPOSE 5678


# run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


FROM weather_challenge_dev
