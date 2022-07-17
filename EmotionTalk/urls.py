from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from EmotionTalk import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('EmotionTalk.emotion_talk_app.urls')),
    path('auth/', include('EmotionTalk.auth_app.urls')),
    path('api-token-auth/', views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
