from rest_framework import serializers

from webapp import models

class ProjectTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProjectTemplate
        fields = "__all__"