from rest_framework import serializers

from app.finance.models import Account, Tag, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class TransactionListSerializer(serializers.HyperlinkedModelSerializer):
    tag = TagInlineSerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'tag', 'amount', 'description', 'created_at')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

