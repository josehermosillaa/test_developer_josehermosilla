from django.contrib import admin
from .models import Proyecto


# Register your models here.
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ["nombre_proyecto", "region"]
    search_fields = ["nombre_proyecto", "region", "id_proyecto"]


admin.site.register(Proyecto, ProyectoAdmin)
