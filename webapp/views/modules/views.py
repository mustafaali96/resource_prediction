from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status as st

from webapp import models
from webapp.serializer.modules_serializer import ModulesSerializer, ProjectTemplateModulesSerializer

class GetAllModulesAPIListView(ListAPIView):
    queryset = models.Modules.objects.all()
    serializer_class = ModulesSerializer


class GetAllModulesByTemplateAPIView(APIView):

    def get(self, request, template_id, *args, **kwargs):
        instances = models.ProjectTemplateModules.objects.get(template_id=template_id)

        serializer = ProjectTemplateModulesSerializer(instance=instances)

        return Response(data=serializer.data, status=st.HTTP_200_OK)

class UpdateModuleView(viewsets.GenericViewSet, UpdateModelMixin):
    queryset = models.Modules.objects.all()
    serializer_class = ModulesSerializer