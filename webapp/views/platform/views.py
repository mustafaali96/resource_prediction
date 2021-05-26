from rest_framework.generics import ListAPIView

from webapp import models
# from webapp.serializer.platform_serializer import PlatformSerializer
from webapp.serializer.platform_type_serializer import PlatformTypeSerializer

class GetPlatformAPIListView(ListAPIView):
    queryset = models.PlatformType.objects.all()
    serializer_class = PlatformTypeSerializer 