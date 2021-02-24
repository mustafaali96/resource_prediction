from rest_framework import serializers

from webapp import models

class PlatformTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlatformType
        fields = '__all__'