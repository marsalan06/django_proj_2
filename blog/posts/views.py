from django.shortcuts import redirect, render
from .models import Category, Posts ,Posts_Form
# Create your views here.

def index(request): 
    form=Posts_Form() #created form object
    data=Posts.objects.all() #retrive data from the model to display
    category=Category.objects.all() #we get all data of category 
    if request.method=='POST':
        form=Posts_Form(request.POST)
        if form.is_valid():
            # data=Posts(
            #     title=request.POST['title'],
            #     content=request.POST['content'],
            # )
            form.save()
            return redirect('/')
    return render(request,'index.html',{'title':'Add New Post','form':form,'rows':data,'cats':category}) 
    #route rendered, cat has the category data to show , we add this from admin panel 
