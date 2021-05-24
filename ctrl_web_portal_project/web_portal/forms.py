from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import AccountModel
from .models.company_models import CompanyModel
from phonenumber_field.modelfields import PhoneNumberField


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


class CreateCompanyForm(forms.ModelForm):
    """ Define the required fields for adding a new company """
    company_name = forms.CharField(max_length=1024)
    phone = PhoneNumberField(null=False,
        blank=False,
        unique=True
    )
    address = forms.CharField(max_length=1024)
    city = forms.CharField(max_length=1024)
    state = forms.CharField(max_length=1024)
    zip_code = forms.CharField(max_length=12)
    country = forms.CharField(max_length=50)

    class Meta:
        model = CompanyModel
        fields = ["company_name", "address", "city", "state", "zip_code", "country", "phone"]

class UpdateCompanyForm(forms.ModelForm):
    """ Update the selected company """
    company_name = forms.CharField(max_length=1024)
    phone = PhoneNumberField(null=False,
        blank=False,
        unique=True
    )
    address = forms.CharField(max_length=1024)
    city = forms.CharField(max_length=1024)
    state = forms.CharField(max_length=1024)
    zip_code = forms.CharField(max_length=12)
    country = forms.CharField(max_length=50)

    class Meta:
        model = CompanyModel
        fields = ["company_name", "address", "city", "state", "zip_code", "country", "phone"]

