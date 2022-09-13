from django_filters import rest_framework as filters
import django_filters

from .models import Offer

class OfferFilter(filters.FilterSet):
    """Класс для фильтрации по входным данным из адресной строки"""
    
    rate_min = django_filters.NumberFilter(field_name="rate_min", lookup_expr='gte')
    rate_max = django_filters.NumberFilter(field_name="rate_max", lookup_expr='lte')
    price = django_filters.NumberFilter(field_name="payment_max", lookup_expr='gte')
    price = django_filters.NumberFilter(field_name="payment_min", lookup_expr='lte')
    term = django_filters.NumberFilter(field_name="term_max", lookup_expr='gte')
    term = django_filters.NumberFilter(field_name="term_min", lookup_expr='lte')

    class Meta:
        model = Offer
        fields = ('rate_min', 'rate_max', 'price', 'term')

