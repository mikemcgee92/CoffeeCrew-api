from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from coffeecrewapi.views import Recipes, Categories, Ingredients, square, CompletedOrders

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"recipes", Recipes, "recipe")
router.register(r"categories", Categories, "category")
router.register(r"ingredients", Ingredients, "ingredient")
router.register(r"completed-orders", CompletedOrders, "completed-order")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('square/orders/', square.get_orders, name='get_orders' ),
    path('', include(router.urls)),
]
