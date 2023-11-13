release: python manage.py makemigrations && python manage.py migrate
web: gunicorn avenue_louise.wsgi:application