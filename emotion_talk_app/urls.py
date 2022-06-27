from django.urls import path

from EmotionTalk.emotion_talk_app.views import GetEmotionFromRecordingView

urlpatterns = [
    path('emotion-recognize/<int:user_id>', GetEmotionFromRecordingView.as_view(), name='emotion recognize'),
]
