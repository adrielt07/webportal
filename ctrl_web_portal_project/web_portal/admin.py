from django.contrib import admin
from web_portal.models.account_models import AccountModel
from web_portal.models.company_models import CompanyModel

# Register your models here.
class AccountModelAdmin(admin.ModelAdmin):
    list_display = ("id", "firstname", "lastname")

class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ("company_name",)

admin.site.register(AccountModel, AccountModelAdmin)
admin.site.register(CompanyModel, CompanyModelAdmin)

