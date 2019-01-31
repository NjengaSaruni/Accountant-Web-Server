from rest_framework import serializers

from app.core.mixins import CreateUpdateMixin
from app.finance.models import Account, Tag, Transaction


class AccountSerializer(CreateUpdateMixin, serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class TagSerializer(CreateUpdateMixin, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class TransactionListSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagInlineSerializer(read_only=Tag)

    class Meta:
        model = Transaction
        fields = ('id', 'tag', 'amount', 'description')


class TransactionSerializer(CreateUpdateMixin, serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'