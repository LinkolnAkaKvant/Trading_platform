from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from retail.models import TradeNetwork


class TradeNetworkForm(forms.ModelForm):
    class Meta:
        model = TradeNetwork
        fields = '__all__'
        widgets = {
            'supplier': ForeignKeyRawIdWidget(TradeNetwork._meta.get_field('supplier').remote_field, admin.site),
        }
