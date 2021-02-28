from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField


class LocationModel(models.Model):
    name = models.CharField(
        "Location Name",
        max_length=1024,
        default=""
    )
    address = models.CharField(
        "Address line 1",
        max_length=1024, 
        default=""
    )
    city = models.CharField(
        "City",
        max_length=1024,
        default=""
    )
    zip_code = models.CharField(
        "ZIP / Postal code", 
        max_length=12, 
        default=""
    )
    country = CountryField(
        blank_label='(select country)',
        default=""
    )
