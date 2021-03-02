from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from web_portal.models.company_models import CompanyModel


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
    state = models.CharField(
        "State", 
        max_length=1024, 
        default=""
    )
    country = CountryField(
        blank_label='(select country)',
        default=""
    )

    company = models.ForeignKey(
        CompanyModel, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.address}"

    class Meta:
        db_table = "location_db"
