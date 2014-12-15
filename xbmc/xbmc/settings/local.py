from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.email.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'xbmc.db'),
    },

    'xbmc': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'MyVideos75.db'),
    }
    
}

DATABASE_ROUTERS = (
    'support.routers.AppRouter',
)

DATABASE_APPS_MAPPING = {
    'showcase': 'xbmc'
}

#INSTALLED_APPS += ("debug_toolbar",)

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': 'INFO',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'alchemy.accounts.models': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}

