from django.shortcuts import render
from slugs.battle.models import Battle 


def battle_board(request):
    context = {} 

    return render(request, "battle/battle_board.html", context=context)


def battle_room(request, battle_id):
    battle = Battle.objects.get(id=battle_id)
    context = {
        "battle": battle,
        "battle_id": battle.id,
    } 

    return render(request, "battle/battle_room.html", context=context)