import django
from django.contrib.messages.constants import INFO
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages #message app imported
from django.contrib.auth import authenticate, login as authorize #to avoid confusion
from django.contrib.auth import logout as deauth #for the logout method
# Create your views here.
def login(request):
    if (request.method=='POST'):
        form=AuthenticationForm() #object made
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Username or password isnt correct")
            return redirect('/user/login')
        else:
            authorize(request,user) #if the user exist it is autherized aka login
            return redirect('/user/profile')
    else:
        if (request.user.is_authenticated):
            return redirect('/user/profile') #if the user is autherized and profile is shown, when we return back
            #we use the same user to redict to its profile rather than showing the form
        #if the above if case fails than only we show the login form again

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

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        messages.info(request,'you need to login first')
        return redirect('/user/login')

def logout(request):
    if request.user.is_authenticated:
        deauth(request) #logout the user already logged in
        messages.info(request,'You have been logged out')
    return redirect('/user/login')