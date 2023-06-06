from django.urls import path

from .views import HomeView, FilmsView, SerialsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('films', FilmsView.as_view(), name='films'),
    path('serials', SerialsView.as_view(), name='serials'),
]
