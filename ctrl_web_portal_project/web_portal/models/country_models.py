from django.db import models
from django.urls import reverse

class CountryModel(models.Model):
    country_name = models.CharField(max_length=64)

    def __str__(self):
        return self.country_name

    class Meta:
        db_table = "country_db"
