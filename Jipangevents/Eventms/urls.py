from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    
   path('custom-login/', views.custom_login, name='custom_login'),
    path('', views.home, name='home'),
     path('home/', views.home, name='home'),
    path('signup/organiser/', views.organiser_signup, name='organiser_signup'),
    path('signup/attendee/', views.attendee_signup, name='attendee_signup'),
    
    

]

