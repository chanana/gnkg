release: python manage.py migrate
web: gunicorn gnkg.wsgi
worker: celery -A gnkg worker --loglevel=info
