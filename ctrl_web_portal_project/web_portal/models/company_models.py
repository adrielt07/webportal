from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
#from web_portal.models.location_models import LocationModel


class CompanyModel(models.Model):
    company_name = models.CharField(max_length=1024)
    phone = PhoneNumberField(
        null=False,
        blank=False,
        unique=True
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

    state = models.CharField(
        "State",
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

    locations = models.ManyToManyField(
        'LocationModel',
        blank=True,
        related_name="locations",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.company_name

    class Meta:
        db_table = "company_db"
