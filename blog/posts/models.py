from django.db import models
from django import forms
from django.db.models import fields #imported this 

# Create your models here.

class Posts(models.Model): #created this model field
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=models.Manager


class Posts_Form(forms.ModelForm): #to build a form using django and not html
    class Meta: #will get data of the fields=[] only
        model=Posts
        fields=['title','content']
