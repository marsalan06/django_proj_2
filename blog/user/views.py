from django.contrib.messages.constants import INFO
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages #message app imported
# Create your views here.
def login(request):
    form=AuthenticationForm() #create object and pass it as key value pair bellow  
    return render (request,"login.html",{'title':'User login','form':form})

def register(request):
    form=UserCreationForm()#same object created and passed  bellow 
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'USER SUCCESSFULLY REGISTERED')
            return redirect('/user/login') #redirect to the login page 
    return render(request,'register.html',{'title':'User Registration','form':form})