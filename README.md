# Weather challenge - Cristian Bertelegni

The data for this app is taken from [https://openweathermap.org/api]

## Prerequisites to run the application

- Docker
- Docker-compose
- Make

## Application Setup 

- Duplicate the `app/.template.env` to `app/.env`
- Run `make build` in a terminal

## Running the server

Run `make run` and go to [http://0.0.0.0:8000/docs] in your browser to see the swagger UI


## Make comands

- `build`: build the docker image
- `run`: run the app, go to 0.0.0.0:8000/docs to see the swagger UI
- `tests`: run the tests
- `tests.debug`: run the tests in debugging mode
- `coverage`: generate the coverage test report. 
    - Go to `<PATH_TO_PROJECT>/weather_challenge/htmlcov/index.html` in your browser to see the 100% of test coverage.


