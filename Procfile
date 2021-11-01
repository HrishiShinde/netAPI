web: gunicorn netAPi.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput
release: python manage.py runserver --settings=netAPi.settings.develop