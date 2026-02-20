from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
#Read
@login_required
def user_list(request):
    users=CustomUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


#Create 
@login_required
def user_create(request):
    if request.method == "POST":
        form= UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form=UserForm()
    return render(request, 'users/user_form.html',{'form': form})


#update
@login_required
def user_update(request, pk):
    user =get_object_or_404(CustomUser, pk=pk)
    if request.method =="POST":
        form= UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

#Delete
@login_required
def user_delete (request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method =="POST":
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'users': user})



# register
def register(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request,"Register ho gya bhai")
            return redirect('login')
        else:
            print("FORM ERROS: ", form.errors)
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})


#login

def user_login(request):
    if request.method =="POST" :
        form =AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('user_list')
    else:
        form= AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

#logout

def user_logout(request):
    logout(request)
    return redirect('login')