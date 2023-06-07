from django.test import TestCase


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")


class FilmsPageTest(TestCase):
    def test_uses_films_template(self):
        response = self.client.get("/films")
        self.assertTemplateUsed(response, "films.html")

    def test_films_are_passed_to_template(self):
        response = self.client.get("/films")
        self.assertTrue('films' in response.context)


class SerialsPageTest(TestCase):

    def test_uses_serials_template(self):
        response = self.client.get("/serials")
        self.assertTemplateUsed(response, "serials.html")

    def test_serials_are_passed_to_template(self):
        response = self.client.get("/serials")
        self.assertTrue('serials' in response.context)
