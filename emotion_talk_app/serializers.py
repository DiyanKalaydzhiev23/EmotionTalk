from rest_framework import serializers
from EmotionTalk.emotion_talk_app.models import Recording


class RecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        fields = ('recording', 'owner_id')
