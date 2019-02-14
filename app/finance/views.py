from uuid import UUID

import django_filters
from django.utils import timezone
from rest_framework import generics

from app.accounts.models import User
from app.core.mixins import CreatorUpdaterMixin
from app.finance.filters import TransactionFilter
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
    filter_class = TransactionFilter()

    def get_queryset(self, *args, **kwargs):
        queryset = super(TransactionListCreateView, self).get_queryset()

        created_at_gte = self.request.GET.get('created_at_gte')
        if created_at_gte is not None:
            created_at_gte = timezone.datetime.strptime(self.request.GET.get('created_at_gte'), '%Y-%m-%d')
            queryset = queryset.filter(created_at__gte=created_at_gte)

        created_at_lte = self.request.GET.get('created_at_lte')
        if created_at_lte is not None:
            created_at_lte = timezone.datetime.strptime(self.request.GET.get('created_at_lte'), '%Y-%m-%d')
            queryset = queryset.filter(created_at__lte=created_at_lte)

        return queryset

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
