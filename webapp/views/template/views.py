from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from webapp import models
from webapp.serializer.project_template_serializer import ProjectTemplateSerializer

class GetTemplateAPIListView(ListAPIView):
    queryset = models.ProjectTemplate.objects.all()
    serializer_class = ProjectTemplateSerializer     

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        headers = {}
        headers["Access-Control-Allow-Origin"] = "*"
        headers["Access-Control-Allow-Credentials"] = True
        headers["Access-Control-Allow-Headers"] = "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale"
        headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        return Response(data=serializer.data, headers=headers)
        