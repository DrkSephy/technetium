"""
Technetium Project Configuration Settings

Requirements:
1. Install PostgreSQL database
2. Create postgres user and db called 'technetium'
3. Run: `python manage.py synchdb`
"""

###################
# DJANGO SETTINGS #
###################
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


######################
# DATABASES SETTINGS #
######################
DATABASES = {
    "default": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "technetium",
        # Ignore below with sqlite3
        "USER": "technetium",
        # Not used with sqlite3.
        "PASSWORD": "ae2cce3603f1913efb36bf39cb20250c",
        # Set to empty string for localhost.
        "HOST": "localhost",
        # Set to empty string for default. Default PostgreSQL port
        "PORT": "5432",
        # Prevent Database transaction abort error.
        'OPTIONS': {'autocommit': True,},
    }
}


##################
# HOSTS SETTINGS #
##################

# Required if DEBUG is False
# For production server, add host/domain names of allowed hosts
ALLOWED_HOSTS = []

# SITE_ID can be found in Admin site hosts
SITE_ID = 0

# Local time zone for this installation.
TIME_ZONE = 'America/New_York'

# Language code for this installation.
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


##################
# PATHS SETTINGS #
##################
import os

# Full filesystem path to the project.
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Name of the directory for the project.
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]

# Every cache key will get prefixed with this value
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

# URL prefix for static files.
STATIC_URL = "/static/"

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Use a trailing slash!
MEDIA_URL = STATIC_URL + "media/"

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))

# Package/module name to import the root urlpatterns from for the project.
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME

# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static"),
    # Put strings here, like "/home/html/static"
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*+%p8szwv!q2^pyl#z@_lfms1iy5ob9t!d@5ahpdnod387l70n'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Location of Project URLS mapper
ROOT_URLCONF = 'technetium.urls'

# Python dotted path to the WSGI application
WSGI_APPLICATION = 'technetium.wsgi.application'


#######################
# DJANGO APPLICATIONS #
#######################
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'


##########################
# LOGGING CONFIGURATIONS #
##########################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
