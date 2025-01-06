from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Organiser, Attendee

class OrganiserSignupForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    organization_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['full_name', 'organization_name', 'phone_number', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please choose another.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone_number) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits long.")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get('full_name')
        organization_name = cleaned_data.get('organization_name')

        if full_name and organization_name and full_name == organization_name:
            raise forms.ValidationError("Full name and organization name cannot be the same.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # Using email as username
        
        if commit:
            user.save()
            Organiser.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                organization_name=self.cleaned_data['organization_name'],
                phone_number=self.cleaned_data['phone_number'],
                email=self.cleaned_data['email']
            )
        return user


class AttendeeSignupForm(UserCreationForm):
    HONORIFIC_CHOICES = [
        ('Mr', 'Mr.'),
        ('Mrs', 'Mrs.'),
        ('Ms', 'Ms.'),
        ('Dr', 'Dr.'),
        ('Prof', 'Prof.'),
        ('Other', 'Other')
    ]

    honorific = forms.ChoiceField(
        choices=HONORIFIC_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    full_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['honorific', 'full_name', 'phone_number', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please choose another.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone_number) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits long.")
        return phone_number

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']  # Using email as username
        
        if commit:
            user.save()
            Attendee.objects.create(
                user=user,
                honorific=self.cleaned_data['honorific'],
                full_name=self.cleaned_data['full_name'],
                phone_number=self.cleaned_data['phone_number'],
                email=self.cleaned_data['email']
            )
        return user
