from rest_framework import viewsets, mixins
from webapp.serializer.project_serializer import ProjectSerializer, PredictionSerializer
from webapp import models

class CreateProjectViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ProjectSerializer
    queryset = models.Project.objects.all()

class CreateProjectPrediction(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PredictionSerializer
    queryset = models.Prediction.objects.all()
