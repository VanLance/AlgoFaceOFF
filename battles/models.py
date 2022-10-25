from django.db import models

# Create your models here.
class User(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=30)
    date_created = models.DateTimeField('sign up date')

# class Algo ?? 
#   
#  
class Battle(models.Model): #possibly User Algo join
    user1=models.CharField(max_length=50)
    user2=models.CharField(max_length=50)
    user3=models.CharField(max_length=50)
    user4=models.CharField(max_length=50)

# class Winner ?? User & Battle Join table