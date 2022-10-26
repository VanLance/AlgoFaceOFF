from django.db import models
from django.forms import EmailField

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100, validators=[EmailField])#look into email validator
    password=models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now=True)

class Problem(models.Model):
    id = models.IntegerField(primary_key=True)
    question= models.CharField(max_length=500)
    test_file= models.CharField(max_length=500)
  
 
class Battle(models.Model): # User & Problem join
    id = models.IntegerField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    problem= models.ForeignKey(Problem, on_delete=models.CASCADE)

class Answer(models.Model): #user, problem, battle join
    id = models.IntegerField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    problem= models.ForeignKey(Problem, on_delete=models.CASCADE)
    solution = models.CharField(max_length=500)
# class Winner ?? User & Battle Join table