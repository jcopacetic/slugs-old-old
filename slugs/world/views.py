from django.shortcuts import render

from slugs.items.models import ShopItem

def world(request):
    context = {}

    return render(request, 'world/world.html', context=context)


def shop(request):
    available_items = ShopItem.objects.filter(in_market=True)
    context = {
        "items": available_items,
    }

    return render(request, 'world/shop.html', context=context)