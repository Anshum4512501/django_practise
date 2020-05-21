from django.shortcuts import render,reverse
from .forms import RegistrationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class RegistrationFormCreateView(LoginRequiredMixin,CreateView):
    form_class = RegistrationForm
    template_name = 'userauth/register.html'
    raise_exception =False
    success_url = reverse_lazy('userauth:login')



# class SignIn(LoginView):
#     form_class = SignInForm 
#     template_name = 'userauth/signin.html' 
    