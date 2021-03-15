"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
from core.settings.base import *

DJANGO_DB = os.environ.get('DJANGO_DB', DJANGO_DB_SQLITE)
DATABASES = {'default': DATABASES_ALL[DJANGO_DB]}

MIDDLEWARE.remove('organizations.middleware.GetSessionMiddleware')
MIDDLEWARE.append('organizations.middleware.DummyGetSessionMiddleware')
MIDDLEWARE.append('core.middleware.UpdateLastActivityMiddleware')

ADD_DEFAULT_ML_BACKENDS = False

LOGGING['root']['level'] = os.environ.get('LOG_LEVEL', 'DEBUG')

if DEBUG:
    MIDDLEWARE_BASE = MIDDLEWARE
    MIDDLEWARE = [
        # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    MIDDLEWARE.extend(MIDDLEWARE_BASE)

DEBUG_PROPAGATE_EXCEPTIONS = get_bool_env('DEBUG_PROPAGATE_EXCEPTIONS', False)

SESSION_COOKIE_SECURE = False

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

RQ_QUEUES = {}