from django.db import models
from django.forms import EmailField

# Create your models here.
class User(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100, validators=[EmailField])#look into email validator
    password=models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'

class Problem(models.Model):
    # id = models.IntegerField(primary_key=True)
    question= models.CharField(max_length=500)
    test_file= models.CharField(max_length=500)
    def __str__(self):
        return self.question
  
class Battle(models.Model): # User & Problem join
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    problem= models.ForeignKey(Problem, on_delete=models.CASCADE)
    time = models.IntegerField(blank=True, null=True)
    
class UserAnswer(models.Model): #user, problem, battle join
    user=models.ForeignKey(User, on_delete=models.CASCADE,)
    problem= models.ForeignKey(Problem, on_delete=models.CASCADE)
    solution = models.CharField(max_length=500)

class Winner(models.Model): # User & Battle Join table
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    battle = models.ForeignKey(Battle, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.f_name} wins battle {self.battle.id}'