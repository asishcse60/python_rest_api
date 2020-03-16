from adjustdataapp.models import DataSet
from django.db.models import Sum, FloatField
from django.db.models.functions import Cast
from django_filters import Filter,FilterSet,filters


class GroupFilter(Filter):
    def filter(self, qs, values):
        try:
            values = list(values.split(','))
        except:
            return qs
        if values is None:
            return qs
        return qs.values(*values).order_by()


class CpiFilter(Filter):
    def filter(self, qs, value):
        if value:
            return qs.order_by().annotate(cpi=Cast(Sum('spend') / Sum('installs'), FloatField()))
        return qs


class AnnotateFilter(Filter):
    def filter(self, qs, values):
        if values is None:
            return qs
        filterElem = {val: Sum(val) for val in values.split(',')}
        return qs.order_by().annotate(**filterElem)


class DataFilter(FilterSet):
    from_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    to_date = filters.DateFilter(field_name='date', lookup_expr='lte')
    channel = filters.CharFilter(field_name='channel', lookup_expr='exact')

    country = filters.CharFilter(field_name='country', lookup_expr='exact')
    os = filters.CharFilter(field_name='os', lookup_expr='exact')

    group_filter = GroupFilter()
    cpi_filter = CpiFilter()
    annotate_filter = AnnotateFilter()
    
    class Meta:
        model = DataSet
        fields = ['from_date', 'to_date', 'channel', 'country', 'os']















