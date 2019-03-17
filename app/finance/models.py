from django.db import models

from app.core.helpers import random_color
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
    color = models.CharField(
        max_length=7,
        null=True,
        blank=True,
        default=random_color
    )

    def clean(self):
        # All tag names should be in lower case
        self.name = self.name.lower()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.name = self.name.lower()

        super(Tag, self).save()

    class Meta:
        app_label = 'finance'
        unique_together = (
            'name',
            'created_by'
        )

    def __str__(self):
        return '%s - %s' % (self.created_by.full_name, self.name)


class Transaction(AbstractBase):
    """
    This is the most import table in this project.
    All other reports rely on this table as the absolute source of truth.
    All reports are generated from processing of data from this table.
    """
    amount = models.DecimalField(
        help_text='Negative amounts indicate expenses, positive indicate income',
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
        help_text='The associated tag, important for grouping similar '
                  'transactions for better reporting',
        on_delete=models.PROTECT,
        related_name='transactions'
    )
    transaction_date = models.DateTimeField(
        help_text='Transaction date and time could be set to be different '
                  'from the date and time of creation of record in the '
                  'database.',
        auto_now_add=True,
        null=False,
        blank=False
    )
    deleted = models.BooleanField(
        help_text='If this transaction will be factored in in reports',
        default=False,
        null=False,
        blank=False
    )

    class Meta:
        app_label = 'finance'
        ordering = ('-transaction_date',)

    def __str__(self):
        return '%s - %s - %s' % (
            self.account.name if self.account else 'General',
            self.tag.name,
            self.amount
        )