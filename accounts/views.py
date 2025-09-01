from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required

def signupview(request):
    form=UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return render(request,'index.html')
    return render(request,'signup.html',{'form':form})
def loginview(request):
    form=AuthenticationForm()
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return render(request,'index.html')
    return render(request,'login.html',{'form':form})
def logoutview(request):
    logout(request)
    return redirect('login')
@login_required(login_url='/login')
def index(request):
    return render(request, "index.html")
