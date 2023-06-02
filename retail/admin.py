from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from retail.forms import TradeNetworkForm
from retail.models import TradeNetwork, Contact, Product


class ContactInline(admin.TabularInline):
    """
    Inline модель для TradeNetworkAdmin
    """
    model = Contact
    extra = 1


class ProductInline(admin.TabularInline):
    """
    Inline модель для TradeNetworkAdmin
    """
    model = Product
    extra = 1


class TradeNetworkAdmin(admin.ModelAdmin):
    """
    Админ панель для модели TradeNetwork. Имеет фильтрации по городам, ссылки на поставщиков,
     возможность удалять задолженность.
    """
    form = TradeNetworkForm
    list_display = ['title', 'level', 'supplier_link', 'debt', 'created_at']
    list_filter = ['contacts__city']
    actions = ['clear_debt']
    inlines = [ContactInline, ProductInline]

    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse('admin:retail_tradenetwork_change', args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier)
        return '-'

    supplier_link.short_description = 'Supplier'

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request,
                          f"Задолженность перед поставщиком у {queryset.count()} объектов была успешно очищена.")

    clear_debt.short_description = "Очистить задолженность перед поставщиком у выбранных объектов"


admin.site.register(TradeNetwork, TradeNetworkAdmin)


class ContactAdmin(admin.ModelAdmin):
    """
    Админ панель для модели Contact
    """
    list_display = ['network', 'email', 'country', 'city', 'street', 'house_number']
    search_fields = ['email', 'country', 'city']
    list_filter = ['country', 'city']


admin.site.register(Contact, ContactAdmin)


class ProductAdmin(admin.ModelAdmin):
    """
    Админ панель для модели Product
    """
    list_display = ['network', 'title', 'model', 'release_date']
    search_fields = ['title', 'model']
    list_filter = ['release_date']


admin.site.register(Product, ProductAdmin)
