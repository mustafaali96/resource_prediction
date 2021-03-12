from rest_framework import serializers

from webapp import models
from webapp.serializer.project_template_serializer import ProjectTemplateSerializer

class ModulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Modules
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        instances = models.SubModule.objects.filter(module = instance.id)
        data['subModules'] = SubModulesSerializer(instance= instances, many=True).data
        return data
        
class SubModulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SubModule
        exclude = ('module',)



class ProjectTemplateModulesSerializer(serializers.ModelSerializer):

    module = ModulesSerializer(many=True)
    template = ProjectTemplateSerializer()

    class Meta:
        model = models.ProjectTemplateModules
        fields = "__all__"