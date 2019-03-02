from uuid import UUID

from django.utils import timezone
from rest_framework import generics

from app.core.mixins import CreatorUpdaterMixin, GetQuerysetMixin
from app.finance.filters import TransactionFilter
from app.finance.models import Account, Transaction, Tag
from app.finance.serializers import AccountSerializer, TransactionSerializer, TagSerializer, TransactionListSerializer


class AccountListCreateView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class TransactionListCreateView(CreatorUpdaterMixin, GetQuerysetMixin, generics.ListCreateAPIView):
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
            tag, _ = Tag.objects.get_or_create(name=tag, created_by=request.user)
            self.request.data['tag'] = tag.id

        return super(TransactionListCreateView, self).create(request)

    def finalize_response(self, request, response, *args, **kwargs):
        try:
            response.data['tag'] = {
                'id': response.data['tag'],
                'name': Tag.objects.get(id=response.data['tag']).name
            }

        except:
            # Type error will be thrown for lists, which already have correct data
            pass

        return super(TransactionListCreateView, self).finalize_response(request, response, args, kwargs)

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
