from django import forms
from .models import AccountModel
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):

    class Meta:
        model = AccountModel
        fields = ["email", "password"]

    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    model = AccountModel
    widgets = {
        'password': forms.PasswordInput(),
    }


class SignUpForm(UserCreationForm):
    """ Define the required fields in SignUp form """
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = AccountModel
        fields = ["email", "firstname", "lastname", "password1", "password2"]
