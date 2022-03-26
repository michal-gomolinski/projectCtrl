from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify


class User(AbstractUser):
    pass


class Project(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Ticket(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    status = models.CharField(max_length=50)
    created_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_tickets', related_query_name='created_ticket')
    closed_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='closed_tickets', related_query_name='closed_ticket')
    assigned = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_tickets', related_query_name='assigned_ticket')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    closed_at = models.DateField()
