from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
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
    queryset = Info.objects.all()
    serializer_class = serializers.InfoSerializer

    def list(self, request, *args, **kwargs):
        info = self.queryset
        private_counter=0
        public_counter=0
        for data in info.values():
            for key, value in data.items():
                if key == 'sector_ies':
                    if value == 'PRIVADA':
                        private_counter+=1
                    if value == 'OFICIAL':
                        public_counter+=1
        return Response({'privada':private_counter,'oficial':public_counter})
