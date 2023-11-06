from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from slugs.dashboard.models import Dashboard, Inventory, UserShop
from slugs.wallet.models import Wallet, Ledger, LedgerItem
from slugs.items.models import Item, ChestItem
from slugs.pets.pet import RandomPetConstructor
from slugs.achievements.models import Achievement

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
       dashboard = Dashboard.objects.create(user=instance)
       inventory = Inventory.objects.create(dashboard=dashboard)
       shop = UserShop.objects.create(dashboard=dashboard)
       wallet = Wallet.objects.create(dashboard=dashboard)
       ledger = Ledger.objects.create(wallet=wallet)
       wallet.add_amount(300, '1')
       chest = Item.objects.get(name="chest")
       chestitem = ChestItem.objects.create(item=chest, inventory=inventory)
       RandomPetConstructor(dashboard).create_random_pet()
       Achievement.objects.get(id=1).award(dashboard)
        