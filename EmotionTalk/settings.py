import os
import decouple
from pathlib import Path
from EmotionTalk import AI_emotion_recognizer


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', decouple.config('SECRET_KEY'))

DEBUG = os.getenv('DEBUG', False)
DEBUG_WITH_EXTERNAL_DB = os.getenv('DEBUG', False)

ALLOWED_HOSTS = ["127.0.0.1", "emotion-talk.herokuapp.com"]

MY_APPS = [
    'EmotionTalk.auth_app',
    'EmotionTalk.emotion_talk_app'
]

INSTALLED_APPS = [
    "corsheaders",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
] + MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:3000',
)
CORS_ALLOW_HEADERS = (
    'content-disposition', 'accept-encoding',
    'content-type', 'accept', 'origin', 'authorization'
)

ROOT_URLCONF = 'EmotionTalk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EmotionTalk.wsgi.application'

if DEBUG and not DEBUG_WITH_EXTERNAL_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'emotion_talk_db',
            'USER': 'postgres',
            'PASSWORD': 'admin',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_NAME', decouple.config('POSTGRES_NAME')),
            'USER': os.getenv('POSTGRES_USER', decouple.config('POSTGRES_USER')),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', decouple.config('POSTGRES_PASSWORD')),
            'HOST': os.getenv('POSTGRES_HOST', decouple.config('POSTGRES_HOST')),
            'PORT': '5432',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

AUTH_USER_MODEL = 'auth_app.EmotionTalkUser'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUD_NAME', decouple.config('CLOUD_NAME')),
    'API_KEY': os.getenv('API_KEY', decouple.config('API_KEY')),
    'API_SECRET': os.getenv('API_SECRET', decouple.config('API_SECRET'))
}

if DEBUG and not DEBUG_WITH_EXTERNAL_DB:
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
else:
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', decouple.config('CELERY_BROKER_URL'))
    CELERY_RESULT_BACKEND = os.getenv('CELERY_BROKER_URL', decouple.config('CELERY_BROKER_URL'))

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TASK_RESULT_SERIALIZER = 'json'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'quizmasterappteam@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', decouple.config('EMAIL_HOST_PASSWORD'))
EMAIL_PORT = 587

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'EmotionTalk/EmotionTalk/AI_emotion_recognizer/recordings')
MEDIA_URL = '/media/'
