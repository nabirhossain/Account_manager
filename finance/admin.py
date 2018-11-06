from django.contrib import admin
from .models import Accounts
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Accounts)
class PostAdmin(ImportExportModelAdmin):
    list_display = ["__str__",'purpose','acc_type', 'amount', 'created']
    list_per_page = 10
    pass
