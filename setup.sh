#!/bin/bash
environment_name="gnkgtesting"

# assumes you have conda
echo "conda stuff"
echo "+++++++++++"
conda create --name ${environment_name} --yes
conda activate ${environment_name}

echo "install python and other requirements"
echo "+++++++++++++++++++++++++++++++++++++"
conda install python=3.8.5 -y

pip install -r requirements.txt

echo "setup environment variables"
echo "+++++++++++++++++++++++++++"
export DJANGO_DEBUG_VALUE="False"
export REDIS_URL="redis://localhost:6379"

echo "make new secret key"
export DJANGO_SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')

echo "setup django app"
python manage.py makemigrations
python manage.py makemigration dnaStrings
python manage.py migrate

echo "start redis server in background"
redis-server --port 6379 --daemonize yes

echo "should see a PONG"
redis-cli -p 6379 ping

echo "start celery worker in background"
celery -A gnkg worker -f gnkg.celery.log -l DEBUG &

echo "start django server"
python manage.py runserver
