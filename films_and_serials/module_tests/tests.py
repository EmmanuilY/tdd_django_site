
from django.test import TestCase, Client
from myapp.models import Films, Serial


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")
        self.assertTrue('films' in response.context)
        self.assertTrue('serials' in response.context)


class WatchDetailPageTest(TestCase):
    def test_uses_film_detail_template(self):
        response = self.client.get("/watch/film1/")
        self.assertTemplateUsed(response, "watch.html")

    def test_film_are_passed_to_template(self):
        response = self.client.get("/watch/film1/")
        film = response.context['film']
        self.assertTrue('film' in response.context)
        self.assertTrue('poster' in film)
        self.assertTrue('video' in film)

    def test_serial_are_passed_to_template(self):
        response = self.client.get("/watch/serial1/")
        serial = response.context['serial']
        self.assertTrue('serial' in response.context)
        self.assertTrue('poster' in serial)
        self.assertTrue('video' in serial)

    def test_invalid_watch_url_returns_404(self):
        response = self.client.get("/watch/random/")
        self.assertEqual(response.status_code, 404)

class FilmModelTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_see_new_films(self):
        film = Films(name='film_best', url='url', poster='pepe', video='')
        film.save()

        response = self.client.get("/")
        self.assertContains(response, 'film_best')
        self.assertContains(response, 'pepe')

class WatchFilmModelTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_see_new_films(self):
        film = Films(name='film_best', url='url', poster='pepe', video='123')
        film.save()
        response = self.client.get("/watch/url/")
        self.assertContains(response, 'film_best')
        self.assertContains(response, 'pepe')