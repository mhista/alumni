from django.contrib import admin
from .models import Alumni
# Register your models here.


class AlumniAdmin(admin.ModelAdmin):
    list_display=('firstname',
        'year_of_graduation',
        'discipline',
        'subscribed',
        'company_name',)
    list_filter=['year_of_graduation','subscribed']
    search_fields = [
        'firstname',
        'surname',
        'year_of_graduation',
        'discipline',
        'subscribed',
        'company_name',
    ]
admin.site.register(Alumni,AlumniAdmin)