from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db.models import Sum
from django.forms import model_to_dict
from men_data.models import Info
import men_data.api.serializers as serializers

class InfoApiViewSet(ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = serializers.InfoSerializer

class FirstApiViewSet(ModelViewSet):
    queryset = Info.objects.order_by('graduados').reverse()
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
