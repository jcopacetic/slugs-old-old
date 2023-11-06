from django.urls import path 

from slugs.world.views import world, shop

app_name = "world"

urlpatterns = [
    path("", view=world, name="world"),
    path("shop/", view=shop, name="shop"),
]