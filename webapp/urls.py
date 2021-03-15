from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("template/", include("webapp.views.template.urls")),
    path("modules/", include("webapp.views.modules.urls")),
    path("platform/", include("webapp.views.platform.urls")),
    path("region/", include("webapp.views.region.urls")),  
    path("prediction/", include("webapp.views.prediction.urls")),
    path("training/", include("webapp.views.training.urls")),
    path('project/', include("webapp.views.project.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)