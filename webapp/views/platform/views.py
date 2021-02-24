from rest_framework.generics import ListAPIView

from webapp import models
from webapp.serializer.platform_serializer import PlatformSerializer

class GetPlatformAPIListView(ListAPIView):
    queryset = models.Platform.objects.all()
    serializer_class = PlatformSerializer 