import json

from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View
from web_portal.forms import CreateCompanyForm, UpdateCompanyForm
from web_portal.models.company_models import CompanyModel
from web_portal.utils.aws_s3 import S3ClientWebPortal
from web_portal.models.account_models import AccountModel

class CreateCompanyView(View):
    """ Only for admin should have access

    Form to create a new company
    """
    form_class = CreateCompanyForm

    def get(self, request):
        """ GET method:
        
        Render the signup.html 
        """
        form = self.form_class().fields
        context = {
            'title': 'Create Company (Admin Only)'
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
            'title': 'Create Company (Admin Only)'
        }
        context['form'] = form
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            post.s3_prefix = f'{post.id}/{post.company_name}'
            post.save()
            s3 = S3ClientWebPortal(post.id, post.company_name)
            s3.create_folder_in_bucket('decom')
            s3.create_folder_in_bucket('invoice')
            return redirect('list_company')
        else:
            cleaned_data = form.cleaned_data
            context['errors'] = form.errors
            return render(request, 'web_portal/createcompany.html', {'context': context})


class CompanyDetailedView(View):
    """ Detail view for each company """
    form_class = UpdateCompanyForm

    def get(self, request, company_pk):
        form = self.form_class().fields

        access = self.validate_access(request.user, company_pk)
        account_model = AccountModel.objects.filter(company_id=company_pk)

        if access == False:
            return redirect('home')
        else:
            company = CompanyModel.objects.get(pk=company_pk)
            context = {
                'title': 'Company Detail',
                'page_title': 'Company Details',
                'account_model': account_model,
            }
            return render(
                request,
                'web_portal/company_detail.html',
                {'context': context, 'company': company}
            )


    def post(self, request, company_pk):
        company = CompanyModel.objects.get(pk=company_pk)
        form = self.form_class(instance=company, data=request.POST)
        context = {
            'title': 'Company Detail',
            'page_title': 'Company Details',
        }
        context['form'] = form
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('detail_company', company_pk=(company.id))
        else:
            return redirect('detail_company', company_pk=(company.id))


    @staticmethod
    def validate_access(user_obj, company_pk):
        """ Validates if the normal user have access to the company
        If they don't have access, redirect them to homepage

        Also, if the user has is_super_admin automatically give them access 
        
        Arg:
            user <user model>: current user object
            pk   <int>: company's primary key

        Return:
            True <bool>: if the user has access
            False <bool>: if the user doesn't have access
        """
        if user_obj.company.id == company_pk or user_obj.is_super_admin:
            return True
        else:
            return False


class ListCompanyView(View):
    """ 
    ONLY for is_super_admin admins
    
    View all existing companies and their information
    """
    def get(self, request):
        company_models = CompanyModel.objects.all()
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': 'Company List',
            'page_title': 'Company List',
            'company_models': company_models,
        }

        if request.user.is_super_admin:
            return render(
                request,
                'web_portal/company_list.html',
                {'context': context}
            )
        else:
            return redirect('home')
