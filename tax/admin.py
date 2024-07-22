from django.contrib import admin

from tax.models import FiscalYear, IncomeTaxPolicy, IncomeTaxRecord

# Register your models here.
class FiscalYearAdmin(admin.ModelAdmin):
    pass

class IncomeTaxRecordAdmin(admin.ModelAdmin):
    pass

class IncomeTaxPolicyAdmin(admin.ModelAdmin):
    pass

admin.site.register(FiscalYear, FiscalYearAdmin)
admin.site.register(IncomeTaxPolicy, IncomeTaxPolicyAdmin)
admin.site.register(IncomeTaxRecord, IncomeTaxRecordAdmin)
