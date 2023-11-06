from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model 
from slugs.pets.models import PetModel, Move
from slugs.items.models import Item

User = get_user_model()

class Opponent(models.Model):
    pet = models.ForeignKey(PetModel, on_delete=models.CASCADE, related_name="opponent")
    health = models.IntegerField(default=0)


class Battle(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=True)
    opponents = models.ManyToManyField(User, blank=True, related_name="battles")
    opponent_1 = models.ForeignKey(Opponent, on_delete=models.CASCADE, null=True, blank=True, related_name="op_1")
    opponent_2 = models.ForeignKey(Opponent, on_delete=models.CASCADE, null=True, blank=True, related_name="op_2")
    STATUS_OPTIONS = [
        ("1", "active"),
        ("2", "closed"),
    ]
    status = models.CharField(max_length=2, choices=STATUS_OPTIONS, default="1")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def clean(self, *args, **kwargs):
        if self.opponents.count() > 2:
            raise ValidationError("You can't assign more than two opponents")
        super(Battle, self).clean(*args, **kwargs)

    def save(self):
         self.save()
         BattleAction.objects.create(battle=self, sender=self.opponent_1, receiver=self.opponent_2)


class BattleAction(models.Model): 
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE, related_name="actions")
    sender = models.ForeignKey(Opponent, on_delete=models.CASCADE, null=True, blank=True, related_name="sender")
    receiver = models.ForeignKey(Opponent, on_delete=models.CASCADE, null=True, blank=True, related_name="receiver")
    move = models.ForeignKey(Move, on_delete=models.CASCADE, null=True, blank=True, related_name="actions")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True, related_name="actions")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sender.pet.name} uses {self.move.name}'
