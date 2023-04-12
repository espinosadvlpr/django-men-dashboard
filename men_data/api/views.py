from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.forms import model_to_dict
from men_data.models import Info
import men_data.api.serializers as serializers

class InfoApiViewSet(ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = serializers.InfoSerializer

class FirstApiViewSet(ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = serializers.FirstQSerializer

    # def list(self, request, *args, **kwargs):
    #     info = self.queryset
    #     first_question = {}
    #     for data in info.values():
    #         for key, value in data.items():
    #             if key == 'ies':
    #                 first_question[key]= value
    #             if key == 'graduados':
    #                 first_question[key]= value
    #             if key == 'matriculados':
    #                 first_question[key]= value
    #     print(first_question)
    #     serializer = self.serializer_class(info,many=True)
    #     return Response(serializer.data)
