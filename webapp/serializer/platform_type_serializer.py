from rest_framework import serializers
from webapp.serializer.platform_serializer import PlatformSerializer
from webapp import models

class PlatformTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlatformType
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        instances = models.Platform.objects.filter(platform_type = instance.id)
        data['Platforms'] = PlatformSerializer(instance= instances, many=True).data
        return data