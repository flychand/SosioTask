from django.db import models
import datetime
from datetime import datetime

# Create your models here.

class Member(models.Model):
    fullname = models.CharField(max_length=40)
    food = models.CharField(max_length=40)
    clothes = models.CharField(max_length=40)
    housekeeping = models.CharField(max_length=40)
    medicine = models.CharField(max_length=40)
    fun = models.CharField(max_length=40)
    total=models.IntegerField(max_length=20)
   
    datte = models.DateField(max_length=40)

    def __str__(self):
    	#return self.firstname + " " + self.lastname

        return self.fullname + " " + self.food +" "+self.clothes + " "+ self.housekeeping + " "+ self.medicine + " "+self.fun 