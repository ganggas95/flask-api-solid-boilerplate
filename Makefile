run-dev:
	python -B app.py

run-test:
	pytest -vv **/__tests__/

run-create-db:
	FLASK_APP=app.py && flask create-db