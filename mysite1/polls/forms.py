from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )

User = get_user_model()


class UserRegister(UserCreationForm):
    username = forms.CharField(required=True, max_length=40)
    email_id = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=20)
    last_name = forms.CharField(required=True, max_length=20)
    widgets = {
        'password': forms.PasswordInput()
    }


class LoginUser(forms.Form):
    username = forms.CharField(required=True, max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput()
    }

 #   def clean(self, *args, **kwargs):
  #     password = self.cleaned_data.get("password")
   #     user = authenticate(username=username, password=password)
       # if not user:
        #    raise forms.ValidationError("This user does not exist")
        #if not user.check_password(password):
         #   raise forms.ValidationError("Incorrect Password")
        #if not user.is_active:
         #   raise forms.ValidationError("This user is no longer active.")
        #return super(LoginUser, self).clean(*args, **kwargs)
        #return username = forms.CharField(*args, **kwargs)
        #def clean UserRegister(required = tru,  max_length=40)
