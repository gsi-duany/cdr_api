from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import CdrSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import DateFilter, DateRangeFilter
from .models import Cdr
from .filters import CdrFilters

# Create your views here.


class CdrViewSet(viewsets.ReadOnlyModelViewSet):



    queryset = Cdr.objects.all()
    serializer_class = CdrSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('clid', 'src', 'dst', 'disposition')
    filterset_class = CdrFilters
    ordering_fields = ('calldate')
