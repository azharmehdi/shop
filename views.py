from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserCreationForm
from .models import Seller
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import SellerCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('home')  # Replace 'home' with your actual home page URL name
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def become_seller(request):
    if hasattr(request.user, 'seller'):
        messages.info(request, "You're already a seller.")
        return redirect('home')

    if request.method == 'POST':
        form = SellerCreationForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.is_seller = True
            seller.save()
            messages.success(request, 'You are now registered as a seller.')
            return redirect('home')
    else:
        form = SellerCreationForm()
    return render(request, 'seller.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('/')  # or redirect('/') if you want to send them to home instead