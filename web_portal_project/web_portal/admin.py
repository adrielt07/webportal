from django.contrib import admin
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel
from web_portal.models.location_models import LocationModel


# Register your models here.
class AccountModelAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname")


class CompanyModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("id", "company_name",)


class LocationModelAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "city", "zip_code", "country",)


admin.site.register(AccountModel, AccountModelAdmin)
admin.site.register(CompanyModel, CompanyModelAdmin)
admin.site.register(LocationModel, LocationModelAdmin)
