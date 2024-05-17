build:
	docker-compose build
run: build
	docker-compose up
tests:
	docker-compose run --entrypoint "pytest -v --disable-warnings app/tests/$(target)" weather_challenge
tests.debug:
	docker-compose run --publish 5678:5678 --entrypoint "python -u -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m pytest -v --disable-warnings app/tests/$(target)" weather_challenge
coverage:
	docker-compose run --entrypoint "sh -c 'coverage run -m pytest -v --disable-warnings app/tests/ && coverage html'" weather_challenge
