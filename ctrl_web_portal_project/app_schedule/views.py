from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from app_schedule.forms import CreateScheduleForm
from app_schedule.models import ScheduleModel


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
            'title': 'Ctrl-layer Schedule Create',
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
            post = form.save(commit=False)
            post.company_id = request.user.company_id
            post.user = request.user
            post.save()
            return redirect('list_schedule')
        else:
            cleaned_data = form.cleaned_data
            context["errors"] = form.errors
            return render(request, 'schedule/create_schedule.html', {'context': context})
