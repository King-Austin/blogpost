from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

#@login_required(login_url='/login')
def home(request):
    return render(request, template_name='main/home.html')
    

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        try:
                
            if password1 != password2:
                ## Asserting both password are the same
                error_message = 'Passwords do not match'
                messages.error(request, error_message)
                return render (request, 'registration/sign_up.html')

                ## Make username Unique
            if User.objects.filter(username=username).exists():
                error_message = 'Sorry, Username already exists'
                messages.error(request, error_message)
                return render (request, 'registration/sign_up.html')

                ## Make Email unique
            if User.objects.filter(email=email).exists():
                error_message = 'Sorry, Email already exists'
                messages.error(request, error_message)
                return redirect ('signup')
            
        except Exception as error:
            error_message = 'OOPS, something went wrong'
            messages.error(request, error_message)
            
            return render (request, 'registration/sign_up.html')
        
        
        ## when all login conditions are passed
        User.objects.create_user(username=username, email=email, password=password1)

        ## Tag along a Success message to the login page.
        success_message = "Signup Success, Login to your account"
        messages.success(request, success_message)
        ## redirect to the Login page using the reverse method
        return redirect ('login')
    
    return render (request, 'registration/sign_up.html')

def login_user(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        ## Authenticating the user after clicking the button
        client = authenticate(username=username, password=password)
        
        if client is not None:
            login (client)
            return redirect('home')

        else:
            error_message = 'Invalid Username or Password'
            messages.error(request, error_message)
            return render(request, 'registration/login.html')
    
    return render(request, 'registration/login.html')

      