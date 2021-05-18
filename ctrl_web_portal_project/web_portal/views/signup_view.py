import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from web_portal.forms import SignUpForm

class SignupView(View):
    form_class = SignUpForm

    def get(self, request):
        """ GET method:
        
        Render the signup.html 
        """
        form = self.form_class().fields
        context = {
            'title': 'Ctrl-layer Portal Signup'
        }
        context['form'] = form
        return render(request, 'web_portal/signup.html', context)

    def post(self, request):
        """ Signup form Post request

        If the form is valid, redirect the to homepage
        else, render the signup.html 
        
        NOTES:
        Future improvements if the form is invalid:
        What we want: 
            (the user should be alerted with what's wrong
                such as: email already taken - This is Done by django
                password doesn't match) - This is DONE 

            Update it so it's more user friendly with red fonts

            We want a successful message that the user has been created
            Or invitation has been send toe the email address for the 
            user to join/login with the password provided by admin
        """
        form = self.form_class(request.POST)
        context = {
            'title': 'Ctrl-layer Portal Signup'
        }
        context['form'] = form
        if form.is_valid():
            post = form.save(commit=False)
            post.company_id = request.user.company_id
            post.save()
            return redirect('userslist')
        else:
            cleaned_data = form.cleaned_data
            context["errors"] = form.errors
            return render(request, 'web_portal/signup.html', {'context': context})

