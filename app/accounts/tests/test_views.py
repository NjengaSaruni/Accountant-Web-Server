from django.contrib.auth.hashers import make_password
from django.test import TestCase, Client

from app.accounts.models import User


class AccountViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_proper_creation(self):
        response = self.client.post('/api/v1/rest-auth/registration/', {
            'first_name': 'John',
            'last_name': 'Otieno',
            'password1': 'acpas!@#',
            'password2': 'acpas!@#',
            'username': 'johnee@gmail.com',
            'email': 'john@gmail.com'
        })

        self.assertEqual(response.status_code, 201)

    def test_not_matching_passwords(self):
        response = self.client.post('/api/v1/rest-auth/registration/', {
            'first_name': 'John',
            'last_name': 'Otieno',
            'password1': 'acpas!@#',
            'password2': 'acpas!@',
            'username': 'johnee@gmail.com',
            'email': 'john@gmail.com'
        })

        self.assertEqual(response.status_code, 400)

    def test_short_passwords(self):
        response = self.client.post('/api/v1/rest-auth/registration/', {
            'first_name': 'John',
            'last_name': 'Otieno',
            'password1': 'acpas',
            'password2': 'acpas',
            'username': 'johnee@gmail.com',
            'email': 'john@gmail.com'
        })

        self.assertEqual(response.status_code, 400)

    def test_login(self):
        User.objects.create(first_name='Agnes', last_name='Nzani', password=make_password('this!@#'), email='agnesnzani@gmail.com')

        response = self.client.post('/api/v1/rest-auth/login/', {
            'username': 'agnesnzani@gmail.com',
            'password': 'this!@#'
        })

        self.assertEqual(response.status_code, 200)
