from django.db import models

from app.core.models import AbstractBase


class Account(AbstractBase):
    balance = models.DecimalField(
        blank=True,
        default=0,
        decimal_places=2,
        max_digits=100
    )
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    class Meta:
        app_label = 'finance'

    def __str__(self):
        return "%s - %s - %s" % (
            self.created_by.full_name,
            self.name,
            self.balance
        )


class Tag(AbstractBase):
    name = models.CharField(max_length=255)
    description = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'finance'
        unique_together = (
            'name',
            'created_by'
        )

    def __str__(self):
        return '%s - %s' % (self.created_by.full_name, self.name)


class Transaction(AbstractBase):
    amount = models.DecimalField(
        blank=True,
        default=0,
        decimal_places=2,
        max_digits=100
    )
    description = models.TextField()
    account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transactions'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.PROTECT,
        related_name='transactions'
    )

    class Meta:
        app_label = 'finance'

    def __str__(self):
        return '%s - %s - %s' % (self.account.name, self.tag.name, self.amount)
