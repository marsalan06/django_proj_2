from django.shortcuts import redirect, render
from .models import Posts ,Posts_Form
# Create your views here.

def index(request): 
    form=Posts_Form() #created form object
    data=Posts.objects.all() #retrive data from the model to display
    if request.method=='POST':
        form=Posts_Form(request.POST)
        if form.is_valid():
            # data=Posts(
            #     title=request.POST['title'],
            #     content=request.POST['content'],
            # )
            form.save()
            return redirect('/')
    return render(request,'index.html',{'title':'Add New Post','form':form,'rows':data}) #route rendered 
