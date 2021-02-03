from django.contrib import admin
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel
from web_portal.models.location_models import (
    CountryModel,
    StateModel,
    AddressModel
    )


# Register your models here.
class AccountModelAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname")

class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ("id", "company_name",)

class AddressModelAdmin(admin.ModelAdmin):
    list_display = ("street_address", "state", "country", )

class CountryModelAdmin(admin.ModelAdmin):
    list_display = ("country_name",)

class StateModelAdmin(admin.ModelAdmin):
    list_display = ("state_name",)

admin.site.register(AccountModel, AccountModelAdmin)
admin.site.register(CompanyModel, CompanyModelAdmin)
admin.site.register(AddressModel, AddressModelAdmin)
admin.site.register(CountryModel, CountryModelAdmin)
admin.site.register(StateModel, StateModelAdmin)
