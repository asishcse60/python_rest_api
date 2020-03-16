from adjustdataapp.models import DataSet
from rest_framework import serializers
from collections import OrderedDict

from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject


class DataSetSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = OrderedDict()
        fields = self._readable_fields
        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute in [None, '']:
                continue

            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                result[field.field_name] = None
            else:
                result[field.field_name] = field.to_representation(attribute)
        return result

    class Meta:
        model = DataSet
        fields = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'cpi')
