from django.db import models
from slugs.dashboard.models import Dashboard

from config.model_options import TYPE_OPTIONS

# buffs
    # decrease/increase hp
    # decrease/increase attack
    # decrease/increase defense
    # decrease/increase special attack
    # decrease/increase special defense
    # decrease/increase speed
    # decrease/increase accuracy
    # decrease/increase evasion

class Move(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=80)
    type_1 = models.CharField(max_length=2, choices=TYPE_OPTIONS, default="1")
    type_2 = models.CharField(max_length=2, choices=TYPE_OPTIONS, default="1")
    attack_damage = models.IntegerField(blank=True, null=True)
    health =  models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.get_type_1_display()} {self.get_type_2_display()}"


class PetModel(models.Model):
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name="pets")
    PET_TYPES = (
        ("1","TYPE 1"),
        ("2","TYPE 2"),
        ("3","TYPE 3"),
        ("4","TYPE 4"),
        ("5","TYPE 5"),
        ("6","TYPE 6"),
        ("7","TYPE 7"),
        ("8","TYPE 8"),
    )
    type = models.CharField(max_length=10, choices=PET_TYPES, default=1)
    name = models.CharField(max_length=120)
    moves = models.ManyToManyField(Move, blank=True, related_name="pets")
    favorite = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_avatar_url(self):
        return f'images/monsters/slug-{self.type}.png'
    
    def set_favorite(self):
        user_pets = PetModel.objects.filter(dashboard=self.dashboard)
        for item in user_pets:
            if item.favorite == True:
                item.favorite = False 
                item.save()
        self.favorite = True 
        self.save()

class PetStat(models.Model):
    pet = models.OneToOneField(PetModel, on_delete=models.CASCADE, related_name="stats")
    hp_now = models.IntegerField(default=0)
    hp_total = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    special_attack = models.IntegerField(default=0)
    special_defense = models.IntegerField(default=0)  
    accuracy = models.IntegerField(default=0)
    evasion = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pet.name}'s stats"
    




# health
# health_regeneration
# Armor 
# Magic Resistance
# Movement Speed 
# attack Range
# Attack Speed 
    # Base Attack Speed
    # Attack Animation
    # Attack Ratio
    # Bonus Attack Speed
# Unit Radius 
    # gameplay Radius
    # selection radius
    # pathing radius
    # acquisition radius 
# Special Statistics
    # damage Dealt bonus 
    # damage received bonus 
    # healing bonus 



