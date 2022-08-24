from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('first_name','last_name','username','email','age','profile_photo')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','username','email','age','profile_photo')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, label='',widget=forms.TextInput(attrs={"class":"form-control ","placeholder":"username",}))
    password = forms.CharField(max_length=50, label='', widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"password"}))
    remember_me = forms.BooleanField(required=False)
    class Meta:
        model = get_user_model()
        fields = ["username","password","remember_me"]


class UserContactForm(forms.Form):
    first_name = forms.CharField(max_length=128, label='',widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=128, label='', widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    phone_number = forms.CharField(max_length=15, required=False, label='', widget=forms.TextInput(attrs={'placeholder':'Phone Number'}))
    email_address = forms.EmailField(max_length=100, label='', widget=forms.EmailInput(attrs={'placeholder':'Email Address'}))
    message = forms.CharField(max_length=5000, label='', widget=forms.Textarea(attrs={'placeholer':'Write your message here!'}))


