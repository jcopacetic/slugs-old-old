from django.urls import path 

from slugs.battle.views import battle_board, battle_room 

app_name = "battle"

urlpatterns = [
    path("", view=battle_board, name="board"),
    path("live/<int:battle_id>/", view=battle_room, name="room"),
]