import os
import pickle

from EmotionTalk.AI_emotion_recognizer.utils import extract_feature
from EmotionTalk.auth_app.models import Profile
from EmotionTalk.emotion_talk_app.models import Recording


def convert_audio(audio_path, target_path):
    os.system(f"ffmpeg -i {audio_path} -ac 1 -ar 16000 {target_path}")
    os.remove(audio_path)


def parse_arguments(filename):
    import argparse
    parser = argparse.ArgumentParser()

    new_filename = filename.lstrip('v')

    parser.add_argument("audio_path")
    parser.add_argument("target_path")

    args = parser.parse_args([f'EmotionTalk/AI_emotion_recognizer/recordings/{filename}',
                              f'EmotionTalk/AI_emotion_recognizer/recordings/{new_filename}'])
    audio_path = args.audio_path
    target_path = args.target_path

    print("The audio file path is: ", audio_path)

    if os.path.isfile(audio_path) and audio_path.endswith(".wav"):
        if not target_path.endswith(".wav"):
            target_path += ".wav"
        convert_audio(audio_path, target_path)
        return target_path
    else:
        raise TypeError("The audio_path file you specified isn't appropriate for this operation")


def recognize_emotion(filename, owner_id):
    model = pickle.load(open("EmotionTalk/AI_emotion_recognizer/result/mlp_classifier.model", "rb"))

    filename = filename.lstrip('/')
    target_path = parse_arguments(filename)

    features = extract_feature(
        target_path,
        mfcc=True,
        chroma=True,
        mel=True)\
        .reshape(1, -1)

    recording = Recording.objects.get(recording=filename)
    recording.delete()
    os.remove(target_path)

    emotion = model.predict(features)[0]

    user = Profile.objects.get(user_id=owner_id)

    if len(user.last_emotions) == user.MAX_EMOTIONS:
        user.last_emotions.pop(0)

    user.last_emotions.append(emotion)
    user.save()

    return emotion
