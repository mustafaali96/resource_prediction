from rest_framework.generics import ListAPIView

from webapp import models
from webapp.serializer.region_serializer import RegionSerializer

class GetRegionAPIListView(ListAPIView):
    queryset = models.Region.objects.all()
    serializer_class = RegionSerializer