from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True) 
    updated_at = models.DateField(auto_now=True)

class Ticket(models.Model):
    title = models.CharField()
    description = models.TextField()
    created_by = models.ForeignKey(User, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True) 
    updated_at = models.DateField(auto_now=True)