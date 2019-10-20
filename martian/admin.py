from django.contrib import admin
from .models import entry
from import_export.admin import ImportExportModelAdmin


@admin.register(entry)
class ViewAdmin(ImportExportModelAdmin):
    pass
