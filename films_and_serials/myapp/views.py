from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class FilmsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'films.html')


class SerialsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'serials.html')
