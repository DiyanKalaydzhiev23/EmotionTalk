from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.authtoken import views
from EmotionTalk import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('EmotionTalk.emotion_talk_app.urls')),
    path('auth/', include('EmotionTalk.auth_app.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
