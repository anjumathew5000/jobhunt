from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_CEO = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_intern = models.BooleanField(default=False)
    is_projectlead=models.BooleanField(default=False)

class InternProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='intern_profile')
	bio = models.CharField(max_length=30,blank=True)
	location = models.CharField(max_length=30,blank=True)
  
class HRProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='hr_profile')
    company_name = models.CharField(max_length=100, blank=True)
    
class CEOProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='ceo_profile')
    CEO_name = models.CharField(max_length=100, blank=True)
class ProjectleadProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='pro_profile')
    lead_name = models.CharField(max_length=100, blank=True)
    lead_project = models.CharField(max_length=100, blank=True)
class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='emp_profile')
    emp_name = models.CharField(max_length=100, blank=True)
    emp_project = models.CharField(max_length=100, blank=True)
   
	
	