import os
from pathlib import Path
from EmotionTalk import AI_emotion_recognizer

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-+c8w!bti-rb1+ifig$*3cvabprl_07ygi9uy)%*vcr92v*aoz$'

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

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
    'http://localhost:3000',
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

if not DEBUG:
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
            'NAME': 'dci07p0afko749',
            'USER': 'ejgfvcvtjupxuu',
            'PASSWORD': 'a7c6228db8a2c94ed9ca15e0cf3b7f174f5ecb836ea1f7ea31146062c6aa8a35',
            'HOST': 'ec2-54-228-32-29.eu-west-1.compute.amazonaws.com',
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
    'CLOUD_NAME': 'dhqp5qtsw',
    'API_KEY': '593912372856725',
    'API_SECRET': 'iedqyBTS3_zeKMh0t1vR7HjkpZA',
}
if not DEBUG:
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
else:
    CELERY_BROKER_URL = 'redis://default:Lgd9A06cD6i9AgxFSblzBoid1QWTmjNk@redis-15182.c300.eu-central-1-1.ec2.cloud.redislabs.com:15182'
    CELERY_RESULT_BACKEND = 'redis://default:Lgd9A06cD6i9AgxFSblzBoid1QWTmjNk@redis-15182.c300.eu-central-1-1.ec2.cloud.redislabs.com:15182'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_TASK_RESULT_SERIALIZER = 'json'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'quizmasterappteam@gmail.com'
EMAIL_HOST_PASSWORD = 'pwxlnzwtlpgfxozt'
EMAIL_PORT = 587

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'EmotionTalk/EmotionTalk/AI_emotion_recognizer/recordings')

# URL used to access the media
MEDIA_URL = '/media/'