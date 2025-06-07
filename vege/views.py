from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def recipe(request):
    if request.method=='POST':
        data=request.POST
        recipe_name=data.get("recipe_name")
        recipe_description=data.get("recipe_description")
        recipe_image=request.FILES.get("recipe_image")
       
        #here objects c reatged by defing function 
        Recipe.objects.create(
            recipe_description=recipe_description,
            recipe_image=recipe_image,
            recipe_name=recipe_name,
        )

        return redirect("/reci/")

    q=Recipe.objects.all()

    if request.GET.get('search'):
        q=queryset.filter(recipe_name__icontains =request.GET.get('search'))
    context={'recipes':q}    

    return render(request,'recipe.html',context)

def delete_receipe(request,id):
    q=Recipe.objects.get(id=id)
    q.delete()
    return redirect('/reci/')

def update_receipe(request,id):
    q=Recipe.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        recipe_name=data.get("recipe_name")
        recipe_description=data.get("recipe_description")
        recipe_image=request.FILES.get("recipe_image")
        q.recipe_name=recipe_name
        q.recipe_description= recipe_description
        if recipe_image:
            q.recipe_image=recipe_image
        
        q.save()
        return redirect('/reci/')



    context={'recipe':q} 
    return render(request,'update.html',context)

    