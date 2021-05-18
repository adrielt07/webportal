from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from app_schedule.models import ScheduleModel


class ScheduleView(View):
    def get(self, request):
        schedules = ScheduleModel.objects.filter(company_id=request.user.company_id)
        context = {
            'firstname': request.user.firstname,
            'lastname': request.user.lastname,
            'title': 'Ctrl-layer Portal Home',
            'page_title': 'Schedule List',
            'schedules': schedules,
        }
        return render(request, 'schedule/schedule_list.html', {'context': context})
