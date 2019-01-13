from rest_framework import serializers

from app.core.mixins import CreateUpdateMixin
from app.finance.models import Account, Tag, Transaction


class AccountSerializer(CreateUpdateMixin, serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'