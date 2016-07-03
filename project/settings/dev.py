# Local
from .base import *

ALLOWED_HOSTS = [
    'localhost:4200 ',
]

# Static Server Config
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_URL = '/static/'

# Media (aka File Upload) Server Config
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_URL = '/media/'

# Aliasing Django Defaults
DEFAULT_FILE_STORAGE = MEDIA_STORAGE
STATICFILES_STORAGE = STATIC_STORAGE

# CORS Settings
CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
)

# Test Settings
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--nologcapture',
    '--with-coverage',
    '--cover-package=apps.api',
]

# Email
DEFAULT_FROM_EMAIL = 'admin@barberscore.com'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    'version': 1,
    "disable_existing_loggers": True,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        'apps.api': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
}

INSTALLED_APPS += (
    'debug_toolbar',
    'django_nose',
)
