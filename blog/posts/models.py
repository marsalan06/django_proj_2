import django
from django.db import models
from django import forms
from django.db.models import fields #imported this 
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model): #created this model field
    def min_len(val): #this is the custom validator working 
        if len(val)<=5:
            raise validators.ValidationError("%(val)s Must be grater than 10", params={'val':val})

    title=models.CharField(validators=[min_len],max_length=255) #validation list provided
    #if validator not used in models 

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=models.Manager

    def __str__(self): #returns object as a string 
        return self.title



class Posts(models.Model): #created this model field
    def min_len(val): #this is the custom validator working 
        if len(val)<=9:
            raise validators.ValidationError("%(val)s Must be grater than 10", params={'val':val})

    title=models.CharField(validators=[min_len],max_length=255) #validation list provided
    content=models.TextField(validators=[min_len])
    
    #user=models.OneToOneField(User,on_delete=models.CASCADE,default=1) #new user relation entry given (A)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1) #many to one relation created (C)
    category=models.ManyToManyField(Category,related_name='categories',default=0) #picks up category as the relation   
    #the related name acts to show posts for each categories, add in form field bellow  (D)
    #if validator not used in models 

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=models.Manager

    def __str__(self): #returns object as a string 
        return self.title



class Posts_Form(forms.ModelForm): #to build a form using django and not html
    class Meta: #will get data of the fields=[] only
        model=Posts
        fields=['title','content','user','category'] #user field added from front end (B), category added 

    #this is a non feild validation 
    def clean(self): #for all fields rather than indivual, creates a dictionary   
        fields=self.cleaned_data 
        print(fields)
        keys=list(fields.keys())
        if (len(fields['title'])<=10):
            raise validators.ValidationError(
                "%(val)s Must be grater than 10", params={'val':keys[0]}
            )
        if (len(fields['content'])<=10):
            raise validators.ValidationError(
                "%(val)s Must be greater than 10",params={'val':keys[1]}
            )
