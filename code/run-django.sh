#!/bin/sh

cd /code

until python test_database.py; do
  echo "Database is unavailable - sleeping"
  sleep 1
done

gunicorn proj.wsgi:application --limit-request-line 0 --worker-tmp-dir /dev/shm --preload --config gunicorn_hooks.py --timeout 900 -w 17 -b :9110