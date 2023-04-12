from rest_framework.serializers import ModelSerializer
from men_data.models import Info

class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

    def to_representation(self, instance):
        return instance.toJSON()

class FirstQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['ies','graduados','matriculados']

class SecondQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['sector_ies','graduados']

class ThirdQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['anio','nivel_formacion','graduados']

class FourthQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['programa_academico','graduados']

class FifthQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['departamento_domicilio_ies','graduados']

class SixthQSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = ['anio','metodologia','ies']
