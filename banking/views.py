from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter

from .models import Offer
from .serializers import OfferSerializer
from .filters import OfferFilter

class OfferViewSet(viewsets.ModelViewSet):
    """Класс обработчика для всей обработки запросов: GET, POST, PATCH, DEL, включая фильтрацию и порядок"""
    
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = OfferFilter
    filterset_fields = ('rate_min', 'rate_max', 'price', 'term')
    ordering_param = 'order'
    ordering_fields = ('rate_min', 'rate_max' 'payment_min', 'payment_max')


