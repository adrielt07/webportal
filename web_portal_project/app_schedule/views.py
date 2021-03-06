from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from app_schedule.forms import CreateScheduleForm
from app_schedule.models import ScheduleModel
from web_portal.utils.aws_s3 import S3ClientWebPortal
from datetime import datetime


class ScheduleView(View):
    def get(self, request):
        """ Retrieve list of schedules filted by company_id """
        schedules = ScheduleModel.objects.filter(company_id=request.user.company_id)
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': 'Ctrl-layer Schedule List',
            'page_title': 'Schedule List',
            'schedules': schedules,
        }
        return render(request, 'schedule/schedule_list.html', {'context': context})



class CreateScheduleView(View):

    form_class = CreateScheduleForm

    def get(self, request):
        """ Render an empty form """
        schedules = ScheduleModel.objects.filter(company_id=request.user.company_id)
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': 'Schedule Create',
            'page_title': 'Schedule List',
            'schedules': schedules,
        }
        return render(request, 'schedule/create_schedule.html', {'context': context})

    def post(self, request):
        """ Create schedule form Post request

        Creates a new schedule if the form is valid
        redirects user to list of schedule
        """
        form = self.form_class(request.POST)
        context = {
            'title': 'Create schedule'
        }
        context['form'] = form
        if form.is_valid():
            data = form.data
            time = data['schedule_time']
            date = data['schedule_date']

            datetime_str = f"{date} {time}"
            datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

            post = form.save(commit=False)
            post.company_id = request.user.company_id
            post.user = request.user
            post.schedule_date = datetime_obj
            post.save()
            return redirect('list_schedule')
        else:
            cleaned_data = form.cleaned_data
            context["errors"] = form.errors
            return render(request, 'schedule/create_schedule.html', {'context': context})


class DetailScheduleView(View):
    
    def get(self, request, pk):
        """ Use to view more detail about the schedule """
        schedule = ScheduleModel.objects.get(pk=pk)
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': 'Schedule Detail',
            'page_title': 'Schedule Details',
        }
        return render(request, 'schedule/detail_schedule.html', {'context': context, 'schedule': schedule})

    def post(self, request, pk):
        """ Deletes a schedule based of pk """
        schedule = ScheduleModel.objects.get(pk=pk)
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': 'Schedule Detail',
            'page_title': 'Schedule Details',
        }
        schedule.delete()
        return redirect('/schedule/')
