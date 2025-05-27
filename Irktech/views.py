from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from Irktech.models import Order, Vent, List

class ShowOrdersView(View):
    template_name = "Irktech/show_orders.html"
    
    def get(request, *args, **kwargs):
        orders = Order.objects.all()

        result = ""
        for s in orders:
            result += s.orderNumber + "<br>"


        return HttpResponse(result)

class ShowListsView(View):
    template_name = "Irktech/show_lists.html"
    
    def get(request, *args, **kwargs):
        lists = List.objects.all()

        result = ""
        for s in lists:
            result += s.id + "<br>"


        return HttpResponse(result)

class ShowVentsView(View):
    template_name = "Irktech/show_vents.html"
    
    def get(request, *args, **kwargs):
        vents = Vent.objects.all()

        result = ""
        for s in vents:
            result += s.ventName + "<br>"


        return HttpResponse(result)