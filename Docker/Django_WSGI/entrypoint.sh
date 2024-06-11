#!/bin/sh

python manage.py create_credentials
python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8069

echo 'Django started!'

exec "$@"