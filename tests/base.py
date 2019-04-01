from django.contrib.auth.hashers import make_password
from rest_framework.test import APITestCase, APIClient

from app.accounts.models import User


class BaseTestClass(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.login_url = '/api/v1/rest-auth/login/'
        self.transactions_url = '/api/v1/account/transactions/'
        self.custom_login_url = '/api/v1/users/login/'
        self.custom_register_url = '/api/v1/users/register/'
        self.transaction_data = {
            "amount": 100,
            "description": "string",
            "tag": "tag"
        }
        self.valid_registration__email_data = {
            "email": "kwanj@gmail.com",
            "password": "kwanjkay"
        }
        self.valid_registration__phone_data = {
            "phone_number": "+254703852334",
            "password": "kwanjkay"
        }
        self.valid_registration__email_data = {
            "email": "kwanj@gmail.com",
            "password": "kwanjkay"
        }
        self.invalid_registration__email_data = {
            "email": "kwanjmail.com",
            "password": "kwanjkay"
        }
        self.invalid_registration__phone_data = {
            "phone_number": "+2547038525334",
            "password": "kwanjkay"
        }
        self.no_data = {
            "password": "kwanjkay"
        }
        self.no_password = {
            "phone_number": "+2547038525334"
        }

    def authenticate(self):
        User.objects.create(
            first_name='Agnes',
            last_name='Nzani',
            password=make_password('this!@#'),
            email='agnesnzani@gmail.com')

        response = self.client.post(self.login_url, {
            'email': 'agnesnzani@gmail.com',
            'password': 'this!@#'
        })
        return response.data['key']
