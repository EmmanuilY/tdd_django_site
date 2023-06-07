from django.urls import path

from .views import HomeView, FilmsView, SerialsView, FilmDetailView, SerialDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('films', FilmsView.as_view(), name='films'),
    path('serials', SerialsView.as_view(), name='serials'),
    path("film_detail/<str:pk>/", FilmDetailView.as_view(), name='film_detail'),
    path('serial_detail/<str:pk>/', SerialDetailView.as_view(), name='serial_detail'),
]
