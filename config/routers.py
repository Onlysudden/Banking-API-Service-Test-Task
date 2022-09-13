from posixpath import basename
from rest_framework.routers import DefaultRouter

from banking.views import OfferViewSet

router = DefaultRouter()
router.register(r'offer', viewset=OfferViewSet, basename='offers')

