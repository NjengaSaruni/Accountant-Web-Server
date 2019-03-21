from django.contrib.auth.hashers import make_password
from rest_framework.test import APITestCase, APIClient

from app.accounts.models import User

class BaseTestClass(APITestCase):

    
    def setUp(self):
        self.client = APIClient()
        self.login_url = '/api/v1/rest-auth/login/'
        self.transactions_url = '/api/v1/account/transactions/'
        self.tag_url = '/api/v1/account/tags/'
        self.transaction_data = {
            'amount': 4000,
            'description': 'description',
            'account': 'salary',
            'tag': 'income'
        }
        self.tag_data = {
            'name': 'tag'
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

    
