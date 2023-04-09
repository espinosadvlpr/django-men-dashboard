from rest_framework.serializers import ModelSerializer
from men_data.models import Info

class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['ies','sector_ies','caracter_ies','departamento_domicilio_ies','municipio_domicilio_ies','programa_academico','nivel_academico','nivel_formacion','metodología','sexo','anio','semestre','graduados','matriculados']
