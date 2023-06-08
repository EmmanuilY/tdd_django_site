from django.test import TestCase
from django.contrib.auth.models import User
from myapp.forms import UserRegistrationForm


class RegistrationTest(TestCase):

    def test_form_is_valid(self):
        form = UserRegistrationForm({
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'mypassword123BB&',
            'password2': 'mypassword123BB&'
        })
        self.assertTrue(form.is_valid())

    def test_not_valid_password(self):
        form = UserRegistrationForm({
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'mypassword',
            'password2': 'mypassword'
        })
        self.assertFalse(form.is_valid())

    def test_not_invalid_email(self):
        form = UserRegistrationForm({
            'username': 'newuser',
            'email': 'not-an-email',
            'password1': 'mypassword123BB&',
            'password2': 'mypassword123BB&'
        })
        self.assertFalse(form.is_valid())

    def test_can_save_new_user(self):
        form = UserRegistrationForm({
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'mypassword123BB&',  # Используйте 'password1' и 'password2'
            'password2': 'mypassword123BB&'
        })
        form.is_valid()
        form.save()

        user = User.objects.first()
        self.assertEqual(user.username, 'newuser')
        self.assertEqual(user.email, 'newuser@example.com')