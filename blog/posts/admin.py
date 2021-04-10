from django.contrib import admin
from .models import Posts, Category #imported the model 
# Register your models here.

admin.site.register([Posts,Category]) #registered it 