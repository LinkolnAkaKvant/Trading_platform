from django.urls import path, include
from rest_framework import routers

from retail.views import TradeNetworkViewSet, ContactViewSet, ProductViewSet, TradeNetworkDetailViewSet

router = routers.DefaultRouter()
router.register(r'trade_networks', TradeNetworkViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'products', ProductViewSet)
router.register(r'trade_network_detail', TradeNetworkDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]