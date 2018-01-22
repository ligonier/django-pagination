import os
from django import VERSION as DJANGO_VERSION

BASE_DIR = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

SECRET_KEY = 'fake-key'

INSTALLED_APPS = (
    'linaro_django_pagination',
)

if DJANGO_VERSION >= (1, 8):
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
            ],
        },
    ]
else:
    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
    )
