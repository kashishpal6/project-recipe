from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def recipes(request):
    if request.method == "POST":
     data = request.POST
     print(data)
     recipe_image = request.FILES.get('recipe_image')
     recipe_name=data.get("recipe_name")
     recipe_description=data.get("recipe_description")
     Recipe.objects.create(
        recipe_name=recipe_name,
        recipe_description = recipe_description,
        recipe_image=recipe_image)
     return redirect('/recipesssss/')
    queryset = Recipe.objects.all()
    context = {'recipesssss': queryset}
    return render(request,'recipes/recipesssss.html',context)

