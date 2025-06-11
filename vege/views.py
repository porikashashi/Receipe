from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here. 


@login_required(login_url="/login/")
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
        q=q.filter(recipe_name__icontains =request.GET.get('search'))
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

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')  


        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Username already taken")
            return redirect('/register')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        messages.error(request, "Account created sucessfully")

        return redirect("/register/")


    return render(request,'register.html')




def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.error(request,'invalid username')
            return redirect("/login/")
        user = authenticate(username=username , password=password)
        if user is None:
            messages.error(request,'invalid password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/reci/')

    return render(request,'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')
