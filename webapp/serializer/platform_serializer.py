from rest_framework import serializers

from webapp.serializer.platform_type_serializer import PlatformTypeSerializer
from webapp import models

class PlatformSerializer(serializers.ModelSerializer):
    
    platform_type = PlatformTypeSerializer()
 
    class Meta:
        model = models.Platform
        fields = "__all__"