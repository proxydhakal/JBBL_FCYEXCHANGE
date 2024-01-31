from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.core.models import FCYExchangeRate, FCYRateMaster, CurrencyTable, FCYDenoMasterTable, FCYExchangeRequestMaster,CurrencyTableResource

admin.site.register(FCYRateMaster)
admin.site.register(FCYExchangeRate)
# class FCYDenoMasterTableAdmin(admin.ModelAdmin):
#     list_display = ('currency', 'deno', 'unit', 'rate', 'equivalentNPR', 'status', 'enteredBy', 'enterDate', 'updatedBy', 'updateDate', 'deletedBy', 'deletedDate')

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         # Assuming 'masterid' is the attribute in FCYDenoMasterTable that corresponds to FCYExchangeRequestMaster's id
#         return qs.filter(masterid=request.GET.get('id'))

admin.site.register(FCYDenoMasterTable)

class FCYExchangeRequestMasterAdmin(admin.ModelAdmin):
    list_display = ('refrenceid', 'date', 'preferredBranch', 'totalEquivalentNPR', 'totalEquivalentNPRToWords', 'status', 'action', 'depositedby', 'remarks', 'enteredBy', 'enterDate', 'updatedBy', 'updateDate', 'deletedBy', 'deletedDate')
    search_fields = ['refrenceid', 'preferredBranch', 'status']
    actions = ['approve_selected', 'reject_selected']  # You can define your own actions

    def approve_selected(self, request, queryset):
        # Your logic for approving selected FCYExchangeRequestMaster instances
        pass

    def reject_selected(self, request, queryset):
        # Your logic for rejecting selected FCYExchangeRequestMaster instances
        pass

admin.site.register(FCYExchangeRequestMaster, FCYExchangeRequestMasterAdmin)



class CurrencyAdmin(ImportExportModelAdmin):
    resource_class = CurrencyTableResource

admin.site.register(CurrencyTable, CurrencyAdmin)