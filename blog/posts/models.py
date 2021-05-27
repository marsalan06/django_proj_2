from typing import Tuple
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
    class Meta:
        db_table='Categories'
        verbose_name="Category"
        verbose_name_plural="Categories"


class Posts(models.Model): #created this model field
    def min_len(val): #this is the custom validator working 
        if len(val)<=9:
            raise validators.ValidationError("%(val)s Must be more than 10", params={'val':val})

    title=models.CharField(validators=[min_len],max_length=255) #validation list provided
    content=models.TextField(validators=[min_len])
    
    thumb_nail=models.FileField(upload_to="posts/",null=True) #file field added 

    #user=models.OneToOneField(User,on_delete=models.CASCADE,default=1) #new user relation entry given (A)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1) #many to one relation created (C)
    category=models.ManyToManyField(Category,related_name='categories',default=0) #picks up category as the relation   
    #the related name acts to show posts for each categories, add in form field bellow  (D)
    
    #if validator not used in models 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=models.Manager

    @property
    def get_photo_url(self): #C1
            return "/media/posts/no_img.png"

    def __str__(self): #returns object as a string 
        return self.title
    
    class Meta:
        db_table='Post'
        verbose_name="Post"
        verbose_name_plural="Posts"



class Posts_Form(forms.ModelForm): #to build a form using django and not html
    class Meta: #will get data of the fields=[] only
        model=Posts
        fields=['title','content','thumb_nail','user','category'] #user field added from front end (B), category added 
        #B1
        widgets={
            'title':forms.TextInput(attrs={'class':'form_control','placeholder':'enter title'}), #placeholder to show in box
            'content':forms.TextInput(attrs={'class':'form_control','placeholder':'enter post content'}),
            'thumb_nail':forms.FileInput(attrs={'class':'form_control','multiple':True}),#(AB1)
            'user':forms.Select(attrs={'class':'form_control'}),
            'category':forms.CheckboxSelectMultiple(attrs={'class':'form_control'})
        }
        help_texts={
            'user':'select user',
            'category':'select category'
        } #shows as a help bellow main heading 
        error_messages={

        }
        lables={

        }

    #this is a non feild validation, either use this or upper
    def clean(self): #for all fields rather than indivual, creates a dictionary   
        fields=self.cleaned_data 
        print(fields)
        keys=list(fields.keys())
        if (len(fields['title'])<=10): #if this is envoked other bellow wont 
            raise validators.ValidationError(
                "%(val)s Must be grater than 10", params={'val':keys[0]}
            )
        if (len(fields['content'])<=10):
            raise validators.ValidationError(
                "%(val)s Must be greater than 10",params={'val':keys[1]}
            )


class Gallery(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE) #(AB2)
    images=models.FileField(upload_to="posts/",blank=True,null=True)

    class Meta:
        db_table='Gallery'
        verbose_name='Gallery'
        verbose_name_plural='Galleries'
