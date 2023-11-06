from django.urls import path 

from slugs.dashboard.views import dashboard, shop_manager 

app_name = "dashboard"

urlpatterns = [
    path("", view=dashboard, name="dashboard"),
    path("shop/manager/", view=shop_manager, name="shop-manager"),
]