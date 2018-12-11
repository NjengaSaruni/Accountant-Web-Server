from django.conf import settings
from django.db import models


class AbstractBase(models.Model):
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True
