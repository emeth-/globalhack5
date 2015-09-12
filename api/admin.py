from django.contrib import admin

from api.models import Citation
class CitationAdmin(admin.ModelAdmin):
    list_display = ('id', 'citation_number', 'citation_date', 'first_name', 'last_name', 'date_of_birth', 'defendant_address', 'defendant_city', 'defendant_state', 'drivers_license_number', 'court_date', 'court_location', 'court_address')
    search_fields = ('id', 'first_name', 'last_name', 'court_location', 'drivers_license_number')
admin.site.register(Citation, CitationAdmin)


from api.models import Violation
class ViolationAdmin(admin.ModelAdmin):
    list_display = ('id', 'citation_number', 'violation_number', 'violation_description', 'warrant_status', 'warrant_number', 'status', 'status_date', 'fine_amount', 'court_cost')
    list_filter = ('warrant_status',)
    search_fields = ('id', 'citation_number', 'violation_number', 'warrant_number')
admin.site.register(Violation, ViolationAdmin)
