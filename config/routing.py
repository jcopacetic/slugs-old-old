from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from slugs.battle.consumers import battle_consumer


websocket_urlpatterns = [
    path('ws/battle/<int:battle_id>/', battle_consumer),
]