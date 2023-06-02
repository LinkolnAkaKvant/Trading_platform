import django_filters.rest_framework
from retail.models import TradeNetwork


class CountryFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(field_name='contacts__country')

    class Meta:
        model = TradeNetwork
        fields = ('country',)
