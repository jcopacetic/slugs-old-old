import random
from slugs.pets.models import PetModel, PetStat

class RandomPetConstructor:
    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.pet_type_stats = {
            "1": {"hp_total": 100, "attack": 20, "defense": 10, "speed": 15, "special_attack": 35, "special_defense": 18, "accuracy": 10, "evasion": 10},
            "2": {"hp_total": 80, "attack": 25, "defense": 5, "speed": 20, "special_attack": 35, "special_defense": 18, "accuracy": 10, "evasion": 10},
            "3": {"hp_total": 120, "attack": 15, "defense": 15, "speed": 10, "special_attack": 35, "special_defense": 18, "accuracy": 10, "evasion": 10},
            "4": {"hp_total": 100, "attack": 20, "defense": 10, "speed": 15, "special_attack": 35, "special_defense": 18, "accuracy": 10, "evasion": 10},
            "5": {"hp_total": 80, "attack": 25, "defense": 5, "speed": 20, "special_attack": 35, "special_defense": 18, "accuracy": 10, "evasion": 10},
            "6": {"hp_total": 120, "attack": 15, "defense": 15, "speed": 10, "special_attack": 35, "special_defense": 18, "accuracy": 10, "evasion": 10},
            "7": {"hp_total": 100, "attack": 20, "defense": 10, "speed": 15, "special_attack": 35, "special_defense": 18, "accuracy": 10, "evasion": 10},
            "8": {"hp_total": 80, "attack": 25, "defense": 5, "speed": 20, "special_attack": 35, "special_defense": 18, "accuracy": 10, "evasion": 10},
        }

    def create_random_pet(self):
        # Randomly select a pet type
        pet_type = str(random.randint(1, 8))  # Assumes 8 types, adjust as needed
        favorite = True
        if len(self.dashboard.pets.all()):
            favorite = False
        # Create a new PetModel instance
        pet = PetModel.objects.create(
            dashboard=self.dashboard,
            type=pet_type,
            favorite=favorite,
            name=f"{self.dashboard.user}'s {pet_type} Slug",
        )

        # Create a new PetStat instance and associate it with the pet
        pet_stat = PetStat.objects.create(
            pet=pet,
            hp_now=self.pet_type_stats[pet_type]["hp_total"],
            hp_total=self.pet_type_stats[pet_type]["hp_total"],
            attack=self.pet_type_stats[pet_type]["attack"],
            defense=self.pet_type_stats[pet_type]["defense"],
            speed=self.pet_type_stats[pet_type]["speed"],
            accuracy=self.pet_type_stats[pet_type]["accuracy"],
            evasion=self.pet_type_stats[pet_type]["evasion"],
            # Set other default stat values here
        )

        return pet