from django.shortcuts import redirect, render
from .models import Category, Posts ,Posts_Form,Gallery
# Create your views here.

from django.views.generic import DetailView

def index(request): 
    form=Posts_Form() #created form object
    data=Posts.objects.all() #retrive data from the model to display
    category=Category.objects.all() #we get all data of category 
    if request.method=='POST':
        form=Posts_Form(request.POST,request.FILES) #request.FILES for file data 
        files=request.FILES.getlist('thumb_nail') #get all files(AB3)
        if form.is_valid():
            post=form.save(commit=False)
            form.save()
            for f in files:
                gallery=Gallery(post=post,images=f)
                gallery.save()
            return redirect('data/')
    return render(request,'index.html',{'title':'Add New Post','form':form,'rows':data,'categories':category}) 
    #route rendered, cat has the category data to show , we add this from admin panel 

def data(request):
    data=Posts.objects.all() #retrive data from the model to display
    category=Category.objects.all() #we get all data of category 
    return render(request,'data.html',{'title':'complete data','rows':data,'categories':category})