from django.db import models
from slugs.dashboard.models import Dashboard 


class Achievement(models.Model):
    CATEGORY_CHOICES = [
        ("1", "account"),
        ("2", "shop"),
        ("3", "inventory"),
        ("4", "pets")
    ]
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default="1")
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=190)
    exp = models.IntegerField(default=50)
    limit = models.IntegerField(default=1)

    def __str__(self):
        return self.name 
    
    def award(self, dashboard):
        check = UserAchievement.objects.filter(achievement=self,  dashboard=dashboard).count()
        if check < self.limit:
            UserAchievement.objects.create(achievement=self,  dashboard=dashboard)
    

    

class UserAchievement(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, related_name="achievements")
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name="achievements")