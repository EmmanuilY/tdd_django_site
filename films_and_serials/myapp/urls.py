from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView,  WatchFilmView, WatchSerialView, registration, login_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("watch/film/<str:pk>/", WatchFilmView.as_view(), name='film_detail'),
    path("watch/serial/<str:pk>/", WatchSerialView.as_view(), name='film_detail'),
    path('registration/', registration, name='registration'),
    path('login/',login_view, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)