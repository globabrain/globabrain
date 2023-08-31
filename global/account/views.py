from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from account.models import UserProfile
from django.contrib import auth
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        # firstname = request.POST.get('firstname')
        # lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        
        if password1 == password2:
            if User.objects.filter( email=email).exists():
                messages.error(request, 'Email already exist')
                print("email already exist")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=email, email=email, password=password1)
                user.save()  # Create Account
                
                messages.success(request, 'Account was created successfully for ' + email)
                return redirect('signin')  # Redirect to your login page
        else:
            messages.error (request,'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'account/register.html')


def signin_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')  # Redirect to your home page
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials supplied')
            return redirect('signin')
    else:
        return render(request, 'account/signin.html')


def signout_view(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')  # Redirect to your home page


# def signin_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)3
#             return redirect('home')  # Redirect to your home page
#     else:
#         form = AuthenticationForm()
#     return render(request, 'account/signin.html', {'form': form})



