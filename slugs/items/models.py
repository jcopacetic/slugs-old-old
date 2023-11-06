import random
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from slugs.dashboard.models import Inventory, UserShop
from slugs.pets.models import PetModel
from slugs.pets.pet import RandomPetConstructor

User = get_user_model()


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    value = models.IntegerField(default=0)
    rarity = models.IntegerField(default=0)
    probability = models.DecimalField(default=1.0, decimal_places=1, max_digits=2)
    
    STATUS_CHOICES = [
        ("1", "Normal"),
        ("2", "No Trade"),
    ]
    released_date = models.DateTimeField(blank=True, null=True)
    retirement_date = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 
    
    def get_avatar_url(self):
        return f"images/items/images/item-{slugify(self.id)}.gif"


class FoodItem(Item):
    health = models.IntegerField(default=50)


class UserItem(models.Model):
    item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE, related_name="created")
    in_shop = models.BooleanField(default=False, null=True, blank=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return f'{self.item.name}'
    
    def add_to_shop(self):
        shop_item = ShopItem.objects.create(item=self, shop=self.inventory.dashboard.shop)
        self.in_shop = True
        self.save()

    def remove_from_shop(self):
        shopitem = ShopItem.objects.get(item=self)
        shopitem.delete()
        self.in_shop = False 
        self.save()
    

class ShopItem(models.Model):
    item = models.ForeignKey(UserItem, null=True, blank=True, on_delete=models.CASCADE, related_name="for_sale")
    amount = models.IntegerField(default=0)
    in_market = models.BooleanField(default=False)
    shop = models.ForeignKey(UserShop, on_delete=models.CASCADE, related_name="shop")

    def change_amount(self, amount):
        self.amount = amount 
        self.save()


class SlugItem(UserItem):
    random_number = models.IntegerField(default=0) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('random_number').default = random.randint(1, 8)

    def open(self):
        RandomPetConstructor(self.inventory.dashboard).create_random_pet()
        self.delete()

class CurrencyItem(UserItem):
    amount = models.IntegerField(default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        weights = [10] * 250 + [50] * 500 + [10] * 250
        ran = random.choices(range(1, 1001), weights=weights)[0]
        self._meta.get_field('amount').default = ran

    def open(self):
        self.inventory.dashboard.wallet.add_amount(self.amount, "3")
        self.delete()

class ChestItem(UserItem):
    random_number = models.IntegerField(default=2) 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('random_number').default = random.randint(2, 5)

    def open(self):
        products = list(Item.objects.all())

        for _ in range(self.random_number):
            # Calculate the total weight (sum of probabilities)
            total_weight = sum(item.probability for item in products)
            total_weight_float = float(total_weight)
            rand = random.uniform(0, total_weight_float)

            selected_item = None 
            for item in products:
                item_probability_float = float(item.probability)  # Convert to float
                if rand < item_probability_float:  # Use the float
                    selected_item = item 
                    break 
                rand -= item_probability_float  # Convert to float

            print(selected_item)

            if selected_item.id == 6:
                ChestItem.objects.create(item=selected_item, inventory=self.inventory)
            elif selected_item.id == 7:
                SlugItem.objects.create(item=selected_item, inventory=self.inventory)
            elif selected_item.id == 8:
                CurrencyItem.objects.create(item=selected_item, inventory=self.inventory)
            else:
                UserItem.objects.create(item=selected_item, inventory=self.inventory)

        self.delete()


