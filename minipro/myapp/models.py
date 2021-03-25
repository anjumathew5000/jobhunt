from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    email=models.EmailField(max_length=30,null=True,blank=True)
