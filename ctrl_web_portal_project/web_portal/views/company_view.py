import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from web_portal.forms import CreateCompanyForm
from web_portal.models.company_models import CompanyModel

class CreateCompanyView(View):
    """ Only for ctrl-layer admin should have access

    Form to create a new company
    """
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
            form.save()
            return redirect('list_company')
        else:
            cleaned_data = form.cleaned_data
            context["errors"] = form.errors
            return render(request, 'web_portal/createcompany.html', {'context': context})


class ListCompanyView(View):
    """ 
    ONLY for Ctrl-layer admins
    
    View all existing companies and their information
    """
    def get(self, request):
        company_models = CompanyModel.objects.all()
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': 'Ctrl-layer Company List',
            'page_title': 'All Companies',
            'company_models': company_models,
        }
        return render(request, 'web_portal/company_list.html', {'context': context})

class CompanyDetailView(View):
    """ View for ctrl-layer admins to view more details about the company"""
    pass
