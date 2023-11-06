import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from slugs.dashboard.models import Dashboard 
from slugs.items.models import (
    UserItem, 
    ShopItem, 
    ChestItem, 
    SlugItem,
    CurrencyItem,
)

@login_required
def dashboard(request):
    dashboard = get_object_or_404(Dashboard, user=request.user.id)
    inventory = UserItem.objects.filter(inventory=request.user.dashboard.inventory, in_shop=False)
    shop = ShopItem.objects.filter(shop=request.user.dashboard.shop)
    context = {
        "dashboard": dashboard,
        "inventory": inventory,
        "shop": shop,
    }

    return render(request, 'dashboard/dashboard.html', context=context)


@csrf_exempt  # Remove this decorator in production; it's for testing purposes
@login_required
def shop_manager(request):
    if request.method == 'POST':
        # Read the raw JSON data from the request body
        data = json.loads(request.body.decode('utf-8'))

        action = data.get('action')
        item_id = data.get('item_id')
        
        if action == 'move_to_shop':
            result = move_item_to_shop(item_id)
        elif action == 'move_to_inventory':
            result = move_item_to_inventory(item_id)
        elif action == 'update_price':
            result = update_item_price(item_id, data.get('amount'))
        elif action == 'market_toggle':
            result = update_market_toggle(item_id, data.get('togglevalue'))
        elif action == 'open_chest':
            result = open_chest(item_id)
        elif action == 'open_slug':
            result = open_slug(item_id)
        elif action == 'open_currency':
            result = open_currency(item_id)
        else:
            result = {"error": "Invalid action"}

        return JsonResponse(result, safe=False)

def move_item_to_shop(item_id):
    item = UserItem.objects.get(id=item_id)
    if item:
        item.add_to_shop()
        return {"message": "Item moved to shop successfully"}
    else:
        return {"error": "Item not found or user does not own it"}

def move_item_to_inventory(item_id):
    item = UserItem.objects.get(id=item_id)
    if item:
        item.remove_from_shop()
        return {"message": "Item removed from shop successfully"}
    else:
        return {"error": "Item not found or user does not own it"}

def update_item_price(item_id, amount):
    item = ShopItem.objects.get(id=item_id)
    if item:
        item.change_amount(amount)
        return {"message": "item price has been updated"}
    else:
        return {"error": "item not found or not in shop or does not belong to user"}
    
def update_market_toggle(item_id, togglevalue):
    item = ShopItem.objects.get(id=item_id)
    if item:
        item.in_market = togglevalue 
        item.save()
        return {"message": "item is now on market"}
    else:
        return {"error": "item not found or not in shop or does not belong to user"}
    
def open_chest(item_id):
    item = ChestItem.objects.get(id=item_id)
    if item:
        item.open()
        return {"message": "Chest opened!"}
    else:
        return {"error": "chest doesn't exist or you don't own it!"}
    
def open_slug(item_id):
    item = SlugItem.objects.get(id=item_id)
    if item:
        item.open()
        return {"message": "Slug Added!"}
    else:
        return {"error": "chest doesn't exist or you don't own it!"}
    
def open_currency(item_id):
    item = CurrencyItem.objects.get(id=item_id)
    if item:
        item.open()
        return {"message": "Currency Added Added!"}
    else:
        return {"error": "chest doesn't exist or you don't own it!"}