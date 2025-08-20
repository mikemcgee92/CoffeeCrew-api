from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from coffeecrewapi.views import Recipes

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"recipes", Recipes, "recipe")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
