from django.urls import path

from .views import RegistrationFormCreateView
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'userauth'

urlpatterns = [
    
    path('register/',RegistrationFormCreateView.as_view(),name="register_user"),
     path('login/',LoginView.as_view(template_name = 'userauth/signin.html' ),name="login"),
     path('logout/',LogoutView.as_view(),name="logout"),

]