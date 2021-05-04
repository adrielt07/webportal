from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class CompanyModel(models.Model):
    company_name = models.CharField(max_length=1024)
    phone = PhoneNumberField(
        null=False,
        blank=False,
        unique=True
    )

    address = models.CharField(
        "Address",
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
        "ZIP_code",
        max_length=12,
        default=""
    )

    country = models.CharField(
        "Country",
        max_length=50,
        default=""
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.company_name} - {self.id}"

    class Meta:
        db_table = "company_db"
