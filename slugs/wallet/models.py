from django.db import models
from django.contrib.auth import get_user_model

from slugs.dashboard.models import Dashboard

class Wallet(models.Model):
    dashboard = models.OneToOneField(Dashboard, on_delete=models.CASCADE, related_name="wallet")
    currency = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.dashboard.user.username}'s wallet"
    
    def add_amount(self, amount, source):
        self.currency = self.currency + amount 
        LedgerItem.objects.create(type=source, operation="1", ledger=self.ledger, amount=amount)
        self.save()

    def subtract_amount(self, amount, source):
        if self.currency >= amount:
            self.currency = self.currency - amount 
            LedgerItem.objects.create(type=source, operation="2", ledger=self.ledger, amount=amount)
            self.save()
        else: 
            return False

class Ledger(models.Model):
    wallet = models.OneToOneField(Wallet, on_delete=models.CASCADE, related_name="ledger")


class LedgerItem(models.Model):
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, related_name="item")
    SOURCE_TYPES = [
        ("1", "system"),
        ("2", "shop"),
        ("3", "chest"),
    ]
    type = models.CharField(max_length=2, choices=SOURCE_TYPES, default="1")
    TRANSACTION_TYPES = [
        ("1", "adds"),
        ("2", "takes"),
    ]
    operation = models.CharField(max_length=2, choices=TRANSACTION_TYPES, default="1")
    amount = models.IntegerField(default=0)

