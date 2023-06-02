from rest_framework import serializers

from retail.models import TradeNetwork, Contact, Product


class TradeNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeNetwork
        fields = ['id', 'title', 'level', 'supplier', 'debt', 'created_at']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'email', 'country', 'city', 'street', 'house_number', 'network']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'model', 'release_date', 'network']


class TradeNetworkDetailSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    products = ProductSerializer(many=True)

    class Meta:
        model = TradeNetwork
        fields = ['id', 'title', 'level', 'supplier', 'debt', 'created_at', 'contacts', 'products']
