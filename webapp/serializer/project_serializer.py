from rest_framework import serializers

from webapp import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        exclude = ('start_date',)