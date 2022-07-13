from django.urls import path
from EmotionTalk.auth_app.views import UserCreate, LoginUserView, ProfileView
from EmotionTalk.auth_app import signals


urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/<int:user_id>/<int:user_to_show_id>/', ProfileView.as_view(), name='profile'),
]
