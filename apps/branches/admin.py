from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.branches.models import Branches, BranchesResource


class BranchesAdmin(ImportExportModelAdmin):
    resource_class = BranchesResource
    ordering = ['BranchCode']

admin.site.register(Branches, BranchesAdmin)