web: gunicorn EmotionTalk.wsgi
release: python manage.py migrate
celery: celery -A EmotionTalk worker -l info
