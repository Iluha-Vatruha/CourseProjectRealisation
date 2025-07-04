"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from Irktech.api import OrdersViewset, ListsViewset, VentsViewset, ClientsViewset

from Irktech import views

from Irktech.api import CustomAuthToken


router = DefaultRouter()
router.register("orders", OrdersViewset, basename="orders")
router.register("lists", ListsViewset, basename="lists")
router.register("vents", VentsViewset, basename="vents")
router.register("clients", ClientsViewset, basename="clients")



urlpatterns = [
    path('api/auth/login/', CustomAuthToken.as_view(), name='api_auth_login'),
    path('', views.ShowOrdersView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include (router.urls)),
]
