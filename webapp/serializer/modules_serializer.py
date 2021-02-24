from rest_framework import serializers

from webapp import models
from webapp.serializer.project_template_serializer import ProjectTemplateSerializer

class ModulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Modules
        fields = "__all__"



class ProjectTemplateModulesSerializer(serializers.ModelSerializer):

    module = ModulesSerializer(many=True)
    template = ProjectTemplateSerializer()

    class Meta:
        model = models.ProjectTemplateModules
        fields = "__all__"