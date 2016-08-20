#!/bin/bash
rm -rf conversor/migrations/*
find . -name "*.pyc" -exec rm -vrf {} \;
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
python manage.py makemigrations conversor
python manage.py migrate conversor
python manage.py runserver 127.0.0.1:8000
