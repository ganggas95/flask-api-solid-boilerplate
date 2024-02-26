run-dev:
	python -B app.py

run-test:
	ENV=testing && pytest -vv ./tests/

run-create-db:
	FLASK_APP=app.py && flask create-db