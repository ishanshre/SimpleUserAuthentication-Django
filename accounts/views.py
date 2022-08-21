from django.shortcuts import render
from .forms import CustomUserCreationForm, LoginForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('base:index')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Registeration Successfull"


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"       

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Logged In Successfull"

    def form_valid(self, form):
        remember_me = form.cleaned_data('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)#Automatically closes the session after browser is closed
            self.request.session.modified = True#set modified data in session to be stored
        return super(UserLoginView, self).form_valid(form)
