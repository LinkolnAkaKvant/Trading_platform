from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from retail.filters import CountryFilter
from retail.models import TradeNetwork, Contact, Product
from retail.permissions import IsActiveStaffPermission
from retail.serializers import TradeNetworkSerializer, ContactSerializer, ProductSerializer, \
    TradeNetworkDetailSerializer


class MyPagination(PageNumberPagination):
    """
    Специальный класс назначения пагинации для вью, которые выводят небольшой массив информации.
    """
    page_size = 5


class TradeNetworkViewSet(viewsets.ModelViewSet):
    """
    Вью для работы с торговой сетью, имеет переопределенную функцию perform_update,
    для запрета обновления через API поля DEBT
    """
    queryset = TradeNetwork.objects.all()
    serializer_class = TradeNetworkSerializer
    permission_classes = [IsActiveStaffPermission]
    pagination_class = MyPagination

    def perform_update(self, serializer):
        serializer.validated_data.pop('debt', None)
        super().perform_update(serializer)


class ContactViewSet(viewsets.ModelViewSet):
    """
    Вью для работы с контактами
    """
    queryset = Contact.objects.all()
    permission_classes = [IsActiveStaffPermission]
    serializer_class = ContactSerializer
    pagination_class = MyPagination


class ProductViewSet(viewsets.ModelViewSet):
    """
    Вью для работы с продуктами
    """
    queryset = Product.objects.all()
    permission_classes = [IsActiveStaffPermission]
    serializer_class = ProductSerializer
    pagination_class = MyPagination


class TradeNetworkDetailViewSet(viewsets.ModelViewSet):
    """
    Вью для детального отображения торговой сети с имеющимися контактами и продуктами
    """
    queryset = TradeNetwork.objects.all()
    serializer_class = TradeNetworkDetailSerializer
    permission_classes = [IsActiveStaffPermission]
    filterset_class = CountryFilter

    def perform_update(self, serializer):
        serializer.validated_data.pop('debt', None)
        super().perform_update(serializer)
