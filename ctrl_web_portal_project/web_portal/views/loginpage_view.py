from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from web_portal.forms import LoginForm
from django.contrib.auth import get_user_model
from web_portal.authbackend import EmailAuthBackend
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login



class LoginpageView(View):
    form_class = LoginForm
    template_name = 'web_portal/login.html'
    def get(self, request):
        form = self.form_class().fields
        user = request.user
        if user.is_authenticated:
            return redirect('/home/')
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = EmailAuthBackend().authenticate(request, username=email, password=password)
            django_login(request, user)
            return redirect('/home/')
        else:
            return render(request, self.template_name, {'form': form})

def logout(request):
    pass
    #django_logout(request)


def RegisterPage(request):
    User = get_user_model()
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'web_portal/register.html', context)
