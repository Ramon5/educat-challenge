run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

test:
	pytest -vv . --cov apps/

statics:
	python manage.py collectstatic --noinput

format:
	isort apps/
	black apps/