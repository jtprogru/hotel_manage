set shell := ["zsh", "-cu"]

superuser_login := 'root'
superuser_password := 'toor'
superuser_email := 'admin@hotel-manage.com'

# Show help
default:
    just --list

# Install all dependencies
install:
    poetry install --no-root

# Create default development super user
createsuperuser:
    cd src && \
    DJANGO_SUPERUSER_USERNAME={{superuser_login}} \
    DJANGO_SUPERUSER_PASSWORD={{superuser_password}} \
    DJANGO_SUPERUSER_EMAIL={{superuser_email}} \
    poetry run python manage.py createsuperuser --noinput

# Run Django development server
rundev:
    cd src && poetry run python manage.py runserver

# Generate Django migration
makemigrations:
    cd src && poetry run python manage.py makemigrations

# Apply Django migration
migrate:
    cd src && poetry run python manage.py migrate

# Full upgrade migrations
mig: makemigrations migrate

