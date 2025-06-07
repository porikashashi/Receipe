from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    peoples=[
        {"name":"shashi", "age":22},
        {"name":"prashanth", "age":27},
        {"name":"sukumar", "age":12},
        {"name":"sai", "age":10},
        {"name":"sandeep", "age":18},
        {"name":"ramakrishna", "age":22},
        {"name":"pandu","age":12}

    ]
    for people in peoples:
        print(people)
    return render(request,"index.html", context={'peoples':peoples})
    
 