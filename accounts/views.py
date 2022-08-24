from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm, UserContactForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView
from django.core.mail import send_mail
from django.views.generic import FormView
# Create your views here.
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('base:index')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Registeration Successfull"
    #Using dispatch to restrict register page when user is logged in
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('base:index')
        return super(SignUpView, self).dispatch(request, *args, **kwargs)


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"       

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Logged In Successfull"

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)#Automatically closes the session after browser is closed
            self.request.session.modified = True#set modified data in session to be stored
        return super(UserLoginView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('base:index')
        return super(UserLoginView, self).dispatch(request, *args, **kwargs)


class UserPasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy("accounts:password_reset_done")

class UserContactView(SuccessMessageMixin, FormView):
    form_class = UserContactForm
    template_name = 'accounts/contactus.html'
    success_url = reverse_lazy('base:index')
    def form_valid(self, form):
        send_mail(
            subject = f"Message from {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}",
            message = form.cleaned_data['message'],
            from_email=form.cleaned_data['email_address'],
            recipient_list=['ishan.shrestha356@gmail.com',]
        )
        return super(UserContactView, self).form_valid(form)
        
    
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Message Successfully Sent"