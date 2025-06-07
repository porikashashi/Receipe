from django.db import models

# Create your models here.

class student(models.Model):
    #id = models.ModelField()
    name = models.CharField()
    emial = models.EmailField()
    image = models.TextField()
    age = models.IntegerField(default=18)
    

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=500)