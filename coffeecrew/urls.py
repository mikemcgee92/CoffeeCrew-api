from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from coffeecrewapi.views import Recipes, Categories, Ingredients

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"recipes", Recipes, "recipe")
router.register(r"categories", Categories, "category")
router.register(r"ingredients", Ingredients, "ingredient")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
