from django.urls import path 
from slugs.pets.views import pet_manager 

app_name = 'pets'

urlpatterns = [
    path("", view=pet_manager, name="pet-manager"),
]