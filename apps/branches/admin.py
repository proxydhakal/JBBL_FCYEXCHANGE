from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from apps.branches.models import Branches, BranchesResource, BranchTellorAccount, BranchesTellorAccountResource

class BranchesAdmin(ImportExportModelAdmin):
    resource_class = BranchesResource
    ordering = ['BranchCode']
    list_filter = ['BranchName']
    search_fields = ['BranchCode']
    list_display = ('BranchName', 'BranchCode', 'EmailAddress')

admin.site.register(Branches, BranchesAdmin)

class BranchAccountAdmin(ImportExportModelAdmin):
    resource_class = BranchesTellorAccountResource
    ordering = ['CyDesc']
    list_filter = ['CyDesc']
    search_fields = ['CyDesc']
    list_display = ('CyCode', 'CyDesc', 'MainCode', 'Name')
    
admin.site.register(BranchTellorAccount, BranchAccountAdmin)
