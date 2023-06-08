from django.views import View
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Films, Serial


class HomeView(View):
    def get(self, request, *args, **kwargs):
        films = Films.objects.all()
        serials = Serial.objects.all()
        return render(request, 'home.html', {'films': films, 'serials': serials})


class WatchFilmView(View):

    def get(self, request, *args, **kwargs):
        try:
            film = Films.objects.get(url=kwargs['pk'])
        except Films.DoesNotExist:
            raise Http404("Film does not exist")

        return render(request, 'watch_film.html', {'film': film})


class WatchSerialView(View):
    def get(self, request, *args, **kwargs):
        try:
            serial = Serial.objects.get(url=kwargs['pk'])
        except Films.DoesNotExist:
            raise Http404("Serial does not exist")

        return render(request, 'watch_serial.html', {'serial': serial})


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            #return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    return render(request, 'home.html')

