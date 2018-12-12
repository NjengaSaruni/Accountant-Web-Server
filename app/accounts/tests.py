from django.test import TestCase
from .models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name='James', last_name='Njenga', password='this!@#', email='jamesnjenga@gmail.com')
        User.objects.create(first_name='Agnes', last_name='Nzani', password='this!@#', email='agnesnzani@gmail.com')

    def test_users_have_full_names(self):
        """
        Users have full_names

        """
        james = User.objects.get(email='jamesnjenga@gmail.com')
        agnes = User.objects.get(email='agnesnzani@gmail.com')
        self.assertEqual(james.full_name, 'James Njenga')
        self.assertEqual(agnes.full_name, 'Agnes Nzani')
