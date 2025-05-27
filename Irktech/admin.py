from django.contrib import admin

from Irktech.models import Vent, Order, List, Client


# Register your models here.

@admin.register(Vent)
class VentAdmin(admin.ModelAdmin):
    list_display = ['id', 'ventName', 'picture']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'orderNumber', 'user', 'date']

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'orderNumber']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone']
    