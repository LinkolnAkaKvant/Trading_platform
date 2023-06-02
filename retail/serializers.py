from rest_framework import serializers
from retail.models import TradeNetwork, Contact, Product


class TradeNetworkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с торговыми сетями (создание, обновление, удаление)
    """

    class Meta:
        model = TradeNetwork
        fields = ['id', 'title', 'level', 'supplier', 'debt', 'created_at']


class ContactSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с контактами (создание, обновление, удаление)
    """
    network_title = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ['id', 'email', 'country', 'city', 'street', 'house_number', 'network', 'network_title']

    def get_network_title(self, obj):
        return obj.network.title


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с продуктами (создание, обновление, удаление)
    """
    network_title = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'model', 'release_date', 'network', 'network_title']

    def get_network_title(self, obj):
        return obj.network.title


class TradeNetworkDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детального отображения торговой сети с контактами и продуктами. Создан только для отображения
    """
    contacts = ContactSerializer(many=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = TradeNetwork
        fields = ['id', 'title', 'level', 'supplier', 'debt', 'created_at', 'contacts', 'products']
