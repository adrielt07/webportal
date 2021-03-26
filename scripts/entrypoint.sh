#!/bin/sh

set -e
python manage.py collectstatic --noinput
python manage.py makemigrations web_portal
python manage.py makemigrations
python manage.py migrate
uwsgi --socket :9000 --workers 4 --master --enable-threads --module ctrl_web_portal.wsgi
