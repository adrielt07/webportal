from django import forms
from .models import AccountModel

class LoginForm(forms.Form):

    class Meta:
        model = AccountModel
        fields = ["email", "password"]

    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    model = AccountModel
    widgets = {
        'password': forms.PasswordInput(),
    }

