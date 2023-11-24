from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.core.models import FCYExchangeRate, FCYRateMaster, CurrencyTable, FCYDenoMasterTable, FCYExchangeRequestMaster,CurrencyTableResource

admin.site.register(FCYRateMaster)
admin.site.register(FCYExchangeRate)
admin.site.register(FCYExchangeRequestMaster)
admin.site.register(FCYDenoMasterTable)



class CurrencyAdmin(ImportExportModelAdmin):
    resource_class = CurrencyTableResource

admin.site.register(CurrencyTable, CurrencyAdmin)