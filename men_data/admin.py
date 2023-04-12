from django.contrib import admin
from men_data.models import Info

# Register your models here.
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display=['ies','sector_ies','caracter_ies','departamento_domicilio_ies','municipio_domicilio_ies','programa_academico','nivel_academico','nivel_formacion','metodologia','sexo','anio','semestre','graduados','matriculados']
