from rest_framework import serializers

from webapp import models

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        exclude = ('start_date',)

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prediction
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        return super().__init__(many=many, *args, **kwargs)