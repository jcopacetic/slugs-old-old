from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 


class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="dashboard")
    experience = models.IntegerField(default=0)


class Inventory(models.Model):
    dashboard = models.OneToOneField(Dashboard, on_delete=models.CASCADE, related_name="inventory")


class UserShop(models.Model):
    dashboard = models.OneToOneField(Dashboard, on_delete=models.CASCADE, related_name="shop")

