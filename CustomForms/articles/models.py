from django.db import models
from django import forms
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100,help_text="Title of the page",verbose_name = 'Ariticale Header')
    content=models.TextField()  
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateField(blank=True, null=True)
    created_by=models.CharField(max_length=50)
    modified_by=models.CharField(max_length=50)

