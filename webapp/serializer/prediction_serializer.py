from rest_framework import serializers

from webapp import models

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prediction
        fields = '__all__'