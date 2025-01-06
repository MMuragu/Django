from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import OrganiserSignupForm, AttendeeSignupForm
from django.contrib.auth.models import User


def about(request):
    return render(request, 'Eventms/about.html')

def contact(request):
    return render(request, 'Eventms/contact.html')

def signup(request):
    return render(request, 'Eventms/signup.html')


def home(request):
    return render(request, 'Eventms/home.html')


'''def signup(request):
    return render(request, 'Eventms/signup.html')  # This shows the choice between Organiser/Attendee'''
def signup(request):
    """
    Renders the signup role selection page.
    """
    return render(request, 'Eventms/signup.html')


def organiser_signup(request):
    if request.method == 'POST':
        form = OrganiserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Correct usage
            messages.success(request, 'Successfully registered as an Organiser!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = OrganiserSignupForm()

    return render(request, 'Eventms/signupform.html', {'form': form, 'user_type': 'Organiser'})


def attendee_signup(request):
    if request.method == 'POST':
        form = AttendeeSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Correct usage
            messages.success(request, 'Successfully registered as an Attendee!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AttendeeSignupForm()

    return render(request, 'Eventms/signupform.html', {'form': form, 'user_type': 'Attendee'})


def custom_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=username_or_email)
            username = user.username
        except User.DoesNotExist:
            username = username_or_email

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Correct usage
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email/username or password.')

    return render(request, 'Eventms/login.html')
