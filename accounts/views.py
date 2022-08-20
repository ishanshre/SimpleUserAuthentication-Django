from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# Create your views here.
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('base:index')

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Registeration Successfull"


