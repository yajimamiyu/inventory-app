#!/usr/bin/env bash

set -o errexit

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py shell <<'PY'
import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_ADMIN_USERNAME")
email = os.environ.get("DJANGO_ADMIN_EMAIL")
password = os.environ.get("DJANGO_ADMIN_PASSWORD")

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        print("Superuser created.")
    else:
        print("Superuser already exists.")
PY
