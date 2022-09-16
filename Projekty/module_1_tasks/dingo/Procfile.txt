release: python manage.py migrate
web: waitress dingo.wsgi:application