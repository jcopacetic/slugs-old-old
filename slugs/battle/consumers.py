import json 
from channels.generic.websocket import (
    AsyncWebsocketConsumer,
    WebsocketConsumer,
)
from asgiref.sync import async_to_sync 
from django.contrib.auth import get_user_model 

User = get_user_model() 

from slugs.pets.models import Move
from slugs.battle.models import Battle, BattleAction 


class BattleConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.battle = None
        self.op_1 = None 
        self.op_2 = None 

    def connect(self):
        battle_id = self.scope["url_route"]["kwargs"]["battle_id"]
        self.battle = Battle.objects.get(id=battle_id)
        self.room_group_name = self.battle.name

        self.op_1 = self.battle.opponent_1
        self.op_2 = self.battle.opponent_2

        bops = {
            'type': 'battle_load',
            'op_1': {
                'id': self.op_1.pet.id,
                'name': self.op_1.pet.name,
                'health': self.op_1.health,
                'moves': []
            },
            'op_2': {
                'id': self.op_2.pet.id,
                'name': self.op_2.pet.name,
                'health': self.op_2.health,
                'moves': []
            }
        } 

        for move in self.op_1.pet.moves.all():
            bops["op_1"]["moves"].append({
                "id": move.id,
                "name": move.name,
                "ad": move.attack_damage,
            })
             
        for move in self.op_2.pet.moves.all():
            bops["op_2"]["moves"].append({
                "id": move.id,
                "name": move.name,
                "ad": move.attack_damage,
            })
            
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            bops
        )


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json["action"]
        
        user_id = self.scope["user"].id
        user = User.objects.get(id=user_id)

        battle_id = self.scope["url_route"]["kwargs"]["battle_id"]

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": action,
                "action": action,
                "user": user.username, 
                "battle_id": battle_id
            }
        )

    def battle_load(self, event):

        self.send(text_data=json.dumps(event))


    def make_move(self, event):
        message = ""

        if self.op_1 and self.op_2:
            message = "they exist"
        else:
            message = "nope"

        self.send(text_data=json.dumps({
            'type': event["action"],
            'action': event["action"],
            'user': event["user"],
            'battle_id': event["battle_id"],
            'message': message,
        }))


battle_consumer = BattleConsumer.as_asgi()