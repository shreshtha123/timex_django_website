from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm, NewsLetterForm
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
def home (request):
    # return HttpResponse('<h1>Manav Rachna</h1> ')
    return render(request,'timex/index.html')

def contact(request):
    form=ContactForm()
    # print(form)
    if(request.method=='POST'):
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()        
            #return redirect('home')
            return render (request,'timex/index.html',{'message':'Message Sent Successfully'})
    return render(request,'timex/contacts.html', {'form':form})

def about(request):
    return render(request,'timex/about.html')

def newsletter(request):
    if request.method=='POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'timex/index.html',{'message':'Successfully Subscribed to Newsletter'})
        else:
            return render (request,'timex/index.html',{'message':'Email already exists'})

def verification(request):
    return render(request, 'timex/verification.html')    

@login_required 
def loginuser(request):
    if request.method=='GET':
        return render(request, 'timex/loginuser.html',{'form':AuthenticationForm()})
    else:
        uname = request.POST['username']
        upwd = request.POST['password']
        user = authenticate(request, username=uname, password=upwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'timex/loginuser.html',{'form':AuthenticationForm(),'message':'User Not Found. Try Again'})

def logoutuser(request):
    logout(request)
    return redirect('home')


def signupuser(request):
    if request.method=='GET':
        return render(request, 'timex/signupuser.html',{'form':UserCreationForm()})
    else:
        uname = request.POST['username']
        upwd1 = request.POST['password1']
        upwd2 = request.POST['password2']
        if upwd1==upwd2:
            try:
                user = User.objects.create_user(username=uname,password=upwd2)
                user.save()
                login(request,user)
            except IntegrityError:
                return render(request, 'timex/signupuser.html',{'form':UserCreationForm(),'message':'Username already exists. Choose another one.'})
            else:
                return redirect('home')
        else:
            return render(request, 'timex/signupuser.html',{'form':UserCreationForm(),'message':'Password Mismatch Error'})