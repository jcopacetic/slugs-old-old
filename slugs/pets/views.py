import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from slugs.pets.models import PetModel

@csrf_exempt 
@login_required 
def pet_manager(request):

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        action = data.get('action')
        item_id = data.get('item_id')

        if action == 'set_favorite':
            result = set_favorite(item_id)
        else: 
            result = {"error": "invalid action"}

        return JsonResponse(result, safe=False)
    

def set_favorite(item_id):
    pet = PetModel.objects.get(id=item_id)
    if pet:
        pet.set_favorite()
        return {"message": "Slug is now your favorite!"}
    else: 
        return {"error": "Slug is not found or user does not own it!"}
