from rest_framework.generics import ListAPIView

from webapp import models
from webapp.serializer.project_template_serializer import ProjectTemplateSerializer

class GetTemplateAPIListView(ListAPIView):
    queryset = models.ProjectTemplate.objects.all()
    serializer_class = ProjectTemplateSerializer 