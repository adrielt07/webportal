from django import forms
from django.db import models
from app_schedule.models import ScheduleModel


class CreateScheduleForm(forms.ModelForm):
    """ Define the required fields for adding a new company """
    #schedule_date = models.DateTimeField(blank=True)
    address = models.CharField(
        max_length=1024,
        default=""
    )

    class Meta:
        model = ScheduleModel
        fields = ["schedule_date", "address"]
