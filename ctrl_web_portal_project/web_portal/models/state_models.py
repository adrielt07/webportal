from django.db import models
from django.urls import reverse
from web_portal.models.country_models import CountryModel


class StateModel(models.Model):
    state_name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=4)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.state_name}, {self.short_name}"

    class Meta:
        db_table = "state_db"
