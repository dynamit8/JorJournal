#!/bin/bash
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create superuser if not exists
if [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ]; then
  echo "Creating superuser..."
  python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email="${DJANGO_SUPERUSER_EMAIL}").exists():
    User.objects.create_superuser(
        email="${DJANGO_SUPERUSER_EMAIL}",
        username="${DJANGO_SUPERUSER_USERNAME:-admin}",
        password="${DJANGO_SUPERUSER_PASSWORD}"
    )
END
fi

# Start server
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
