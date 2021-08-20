#!/bin/sh

cd /code

until python test_database.py; do
  echo "Database is unavailable - sleeping"
  sleep 1
done

gunicorn proj.wsgi:application --limit-request-line 0 --config gunicorn_hooks.py --timeout 99999 -w 1 --reload -b :9110