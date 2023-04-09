from rest_framework.viewsets import ModelViewSet
from men_data.models import Info
from men_data.api.serializers import InfoSerializer

class InfoApiViewSet(ModelViewSet):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
