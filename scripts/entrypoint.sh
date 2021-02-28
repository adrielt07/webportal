#!/bin/sh

set -e
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py migrate web_portal
uwsgi --socket :9000 --workers 4 --master --enable-threads --module ctrl_web_portal.wsgi
