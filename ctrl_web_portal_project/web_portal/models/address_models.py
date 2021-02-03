from django.db import models
from django.urls import reverse
from web_portal.models.country_models import CountryModel
from web_portal.models.state_models import StateModel


class AddressModel(models.Model):
    street_address = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=32)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    state = models.ForeignKey(StateModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street_address}"

    class Meta:
        db_table = "address_model"
