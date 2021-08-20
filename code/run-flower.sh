#!/bin/sh

cd /code

until python test_database.py; do
  echo "Database is unavailable - sleeping"
  sleep 1
done

celery -A proj flower --basic_auth=cidc:"cidcdev386"