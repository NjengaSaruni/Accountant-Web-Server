import json
from django.contrib.auth.hashers import make_password

from tests.base import BaseTestClass
from app.finance.models import Transaction
from app.accounts.models import User

class FinanceViewsTestCase(BaseTestClass):

    def test_create_tag(self):
        token = self.authenticate()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(
            self.tag_url,
            data=json.dumps(self.tag_data),
            content_type='application/json'
        )
         # Work in progress

    def test_create_transactions(self):
        token = self.authenticate()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.post(
            self.transactions_url,
            data=json.dumps(self.transaction_data),
            content_type='application/json'
        )
        # Work in progress




    
