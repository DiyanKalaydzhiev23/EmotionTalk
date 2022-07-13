from django.contrib import admin
from EmotionTalk.emotion_talk_app.models import Recording


@admin.register(Recording)
class RecordingAdmin(admin.ModelAdmin):
    pass
