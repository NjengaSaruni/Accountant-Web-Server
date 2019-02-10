from uuid import UUID

from rest_framework import generics

from app.accounts.models import User
from app.core.mixins import CreatorUpdaterMixin
from app.finance.models import Account, Transaction, Tag
from app.finance.serializers import AccountSerializer, TransactionSerializer, TagSerializer, TransactionListSerializer


class AccountListCreateView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class TransactionListCreateView(CreatorUpdaterMixin, generics.ListCreateAPIView):
    queryset = Transaction.objects.all()

    def create(self, request, *args, **kwargs):
        tag = self.request.data.get('tag')
        try:
            tag_uuid = UUID(tag)
        except ValueError:
            user = User.objects.first()
            tag, _ = Tag.objects.get_or_create(name=tag, created_by=user)
            self.request.data['tag'] = tag.id

        return super(TransactionListCreateView, self).create(request)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransactionListSerializer
        return TransactionSerializer


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class TagListCreateView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
