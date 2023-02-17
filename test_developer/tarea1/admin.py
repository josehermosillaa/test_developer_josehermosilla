from django.contrib import admin
from .models import Network, Station


# Register your models here.
class StationAdmin(admin.ModelAdmin):
    search_fields = ["name", "address"]
    list_display = ["name", "address"]


admin.site.register(Network)
admin.site.register(Station, StationAdmin)
