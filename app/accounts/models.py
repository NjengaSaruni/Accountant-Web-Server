from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(null=True, blank=True, max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        if not self.updated_at:
            self.updated_at = timezone.now()
        if not self.username:
            self.username = self.email
        return super(User, self).save()

    @property
    def full_name(self):
        return self.get_full_name()

    def __str__(self):
        return self.email
