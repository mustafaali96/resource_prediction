from rest_framework import serializers

from webapp import models

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Region
        fields = "__all__"