from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


from django.shortcuts import render
from django.views import View

class FilmsView(View):
    def get(self, request, *args, **kwargs):
        test_films = [
            {'name': 'Film1', 'poster': 'https://example.com/images/film1.jpg', 'url': 'film1'},
            {'name': 'Film2', 'poster': 'https://example.com/images/film2.jpg', 'url': 'film2'},
            # Add more test data here
        ]
        return render(request, 'films.html', {'films': test_films})

class SerialsView(View):
    def get(self, request, *args, **kwargs):
        test_serials = [
            {'name': 'Serial1', 'poster': 'https://example.com/images/serial1.jpg', 'url': 'serial1'},
            {'name': 'Serial2', 'poster': 'https://example.com/images/serial2.jpg', 'url': 'serial2'},
            # Add more test data here
        ]
        return render(request, 'serials.html', {'serials': test_serials})

class FilmDetailView(View):
    def get(self, request, *args, **kwargs):
        test_serials = [
            {'name': 'Film1', 'poster': 'https://example.com/images/serial1.jpg', 'url': 'film1'},
            {'name': 'Film2', 'poster': 'https://example.com/images/serial2.jpg', 'url': 'film2'},
            # Add more test data here
        ]
        return render(request, 'films.html', {'films': test_serials})

class SerialDetailView(View):
    def get(self, request, *args, **kwargs):
        test_serials = [
            {'name': 'Serial1', 'poster': 'https://example.com/images/serial1.jpg', 'url': 'serial1'},
            {'name': 'Serial2', 'poster': 'https://example.com/images/serial2.jpg', 'url': 'serial2'},
            # Add more test data here
        ]
        return render(request, 'serials.html', {'serials': test_serials})