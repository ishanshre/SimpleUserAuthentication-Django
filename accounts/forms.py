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
