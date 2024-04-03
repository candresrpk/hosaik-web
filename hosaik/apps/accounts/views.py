from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


def loginView(request):
    context = {
        "form": AuthenticationForm
    }
    if request.method == 'GET':
        return render(request, 'accounts/login.html', context)
    else:
        user = authenticate(
            request, 
            username=request.POST['username'], 
            password=request.POST['password']
        )
        
        if user is None:
            messages.success(request, 'Username or Password is wrong')
            context['message_type'] = 'danger'
            return render(request, 'accounts/login.html', context)
        else:
            login(request, user)
            return redirect('blog:blog')
   
    
def logoutView(request):
    logout(request)
    return redirect('accounts:login')


def registerView(request):
    context = {
        "form": UserCreationForm
    }
    if request.method == 'GET':
        return render(request, 'accounts/register.html', context)
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                messages.success(request, 'User Created')
                return redirect('blog:blog')
            except Exception as e:
                print(e)
                messages.warning(request, 'Ups something went wrong')
                context['message_type'] = 'warning'
                return render(request, 'accounts/register.html', context)
        else:
            messages.warning(request, 'User or password did not match')
            context['message_type'] = 'warning'
            return render(request, 'accounts/register.html', context)