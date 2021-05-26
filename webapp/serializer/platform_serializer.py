from rest_framework import serializers
from webapp import models

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Platform
        fields = "__all__"