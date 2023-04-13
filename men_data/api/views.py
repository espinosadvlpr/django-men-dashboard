from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.forms import model_to_dict
from men_data.models import Info
import men_data.api.serializers as serializers

class InfoApiViewSet(ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = serializers.InfoSerializer

class FirstApiViewSet(ModelViewSet):
    queryset = Info.objects.values('ies').annotate(graduados=Sum('graduados')).annotate(matriculados=Sum('matriculados')).order_by('-graduados')
    serializer_class = serializers.FirstQSerializer

class SecondApiViewSet(ModelViewSet):
    queryset = Info.objects.filter(anio=2019,graduados__gte=1).values('sector_ies').annotate(graduados=Sum('graduados')).order_by()
    serializer_class = serializers.SecondQSerializer

class ThirdApiViewSet(ModelViewSet):
    queryset = Info.objects.values('anio','nivel_formacion').annotate(graduados=Sum('graduados')).order_by('-graduados')
    serializer_class = serializers.ThirdQSerializer

class FourthApiViewSet(ModelViewSet):
    queryset = Info.objects.values('programa_academico').annotate(graduados=Sum('graduados')).order_by('-graduados')
    serializer_class = serializers.FourthQSerializer

class FifthApiViewSet(ModelViewSet):
    queryset = Info.objects.values('departamento_domicilio_ies').annotate(graduados=Sum('graduados')).order_by('-graduados')
    serializer_class = serializers.FifthQSerializer

class SixthApiViewSet(ModelViewSet):
    queryset = Info.objects.values('anio','metodologia').annotate(ies=Count('ies')).order_by('-ies')
    serializer_class = serializers.SixthQSerializer
