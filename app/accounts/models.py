from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return self.get_full_name()

    def __str__(self):
        return self.email
