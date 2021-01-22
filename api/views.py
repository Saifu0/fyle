from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.pagination import (
    LimitOffsetPagination
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.generics import (
    ListAPIView,
)
from .models import Banks, Branches
from .serializers import BankSerializer, BranchSerializer


class BranchListView(ListAPIView):
    serializer_class = BranchSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['ifsc', 'bank__id', 'branch',
                     'address', 'city', 'district', 'state']
    ordering = ['ifsc']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Branches.objects.all()
        query = self.request.GET.get("q")

        if query:
            queryset_list = queryset_list.filter(
                Q(ifsc__icontains=query) |
                Q(bank__id__icontains=query) |
                Q(branch__icontains=query) |
                Q(address__icontains=query) |
                Q(city__icontains=query) |
                Q(district__icontains=query) |
                Q(state__icontains=query)
            ).distinct()
        return queryset_list


class BranchAutocompleteView(ListAPIView):
    serializer_class = BranchSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['branch']
    ordering = ['ifsc']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Branches.objects.all()
        query = self.request.GET.get("q")

        if query:
            queryset_list = queryset_list.filter(branch__icontains=query)

        return queryset_list
