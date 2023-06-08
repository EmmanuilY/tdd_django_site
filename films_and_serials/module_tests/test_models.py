from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from myapp.models import Films, Serial


class FilmModelTest(TestCase):

    def test_cannot_save_films_with_equal_url(self):
        film1 = Films(name='film1', url='url', poster='', video='')
        film2 = Films(name='film2', url='url', poster='', video='')
        with self.assertRaises(IntegrityError):
            film1.save()
            film2.save()


class SerialModelTest(TestCase):

    def test_cannot_save_serials_with_equal_url(self):
        serial1 = Serial(name='serial1', url='url', poster='')
        serial2 = Serial(name='serial2', url='url', poster='')
        with self.assertRaises(IntegrityError):
            serial1.save()
            serial2.save()
