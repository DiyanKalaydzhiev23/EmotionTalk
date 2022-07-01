from django.urls import path
from EmotionTalk.emotion_talk_app.views import GetEmotionFromRecordingView, SearchForUsersView, \
    PendingUsersRequestsView, ReceiveDataUsersView, SendUserRequestView

urlpatterns = [
    path('emotion-recognize/<int:user_id>/', GetEmotionFromRecordingView.as_view(), name='emotion recognize'),
    path('search-for-users/<int:user_id>/', SearchForUsersView.as_view(), name='search for users'),
    path('send-user-request/', SendUserRequestView.as_view(), name='send user request'),
    path('pending-user-requests/<int:user_id>/', PendingUsersRequestsView.as_view(), name='pending user requests'),
    path('receive-data-users/<int:data_user_id>/', ReceiveDataUsersView.as_view(), name='receive data users'),
    path('get-emotion-from-recording/<int:user_id>/', GetEmotionFromRecordingView.as_view(), name='get emotion form recording'),
]
