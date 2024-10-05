from django_filters import rest_framework
from django.utils.functional import lazy
from cats_type.models import CatsType


def get_cat_types():
    return [(cats_type, cats_type) for cats_type in CatsType.objects.all()]


class CatsFilter(rest_framework.FilterSet):
    type = rest_framework.ChoiceFilter(field_name='type__name',
                                       choices = lazy(get_cat_types, list))
    color = rest_framework.CharFilter(field_name='color',
                                      lookup_expr='icontains')
    age = rest_framework.RangeFilter(field_name='age')
