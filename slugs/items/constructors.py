from slugs.items.models import Item, ChestItem

class ChestConstructor:
    def __init__(self, inventory):
        self.inventory = inventory 

    def create_chest(self):
        item = Item.objects.get(name="chest")
        chestitem = ChestItem.objects.create(item=item, inventory=self.inventory)
        return chestitem
