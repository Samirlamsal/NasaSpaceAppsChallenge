from django.contrib import admin
from .models import entry
from .models import data
from import_export.admin import ImportExportModelAdmin


@admin.register(entry)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(data)
class ViewAdmin(ImportExportModelAdmin):
    pass    
