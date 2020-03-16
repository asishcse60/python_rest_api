from rest_framework import generics
from adjustdataapp.serializers import DataSetSerializer
from adjustdataapp.models import DataSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny
from adjustdataapp.datasetfilters import DataFilter
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    last_page_strings = ('last',)


class DataSetListFilter(generics.ListAPIView):
    serializer_class = DataSetSerializer
    queryset = DataSet.objects.all().order_by('id').distinct()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    permission_classes = (AllowAny,)
    filter_class = DataFilter
    ordering_fields = ['date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue',
                       'cpi']

