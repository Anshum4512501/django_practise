from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields  = ['username','email','password1','password2']


    def save(self,commit=True):
        instance   = super(RegistrationForm,self).save(commit=False)
        password1  =  self.cleaned_data['password1']
        password2  =  self.cleaned_data['password2']

        if password1 != password2:
            raise Exception('Not Equal')
        else:
            instance.save()
        return instance    


# class SignInForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password =forms.PasswordInput()





