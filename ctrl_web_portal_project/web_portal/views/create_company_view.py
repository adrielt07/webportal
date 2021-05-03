import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from web_portal.forms import CreateCompanyForm

class CreateCompanyView(View):
    form_class = CreateCompanyForm

    def get(self, request):
        """ GET method:
        
        Render the signup.html 
        """
        form = self.form_class().fields
        context = {
            'title': 'Ctrl-layer Create Company'
        }
        context['form'] = form
        return render(request, 'web_portal/createcompany.html', {'context': context})

    def post(self, request):
        """ Create compnay form Post request

        If the form is valid, add a new company to the database
        redirect the to homepage else, render the createcompany.html 
        """
        form = self.form_class(request.POST)
        context = {
            'title': 'Ctrl-layer Create Company'
        }
        context['form'] = form
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect('login')
        else:
            print("form is invalid")
            cleaned_data = form.cleaned_data
            context["errors"] = form.errors
            return render(request, 'web_portal/createcompany.html', {'context': context})
