from django.urls import path, include
from rest_framework.routers import DefaultRouter

from webapp.views.project import views

router = DefaultRouter()
router.register('post', views.CreateProjectViewSet)
router.register('prediction/post', views.CreateProjectPrediction)

urlpatterns = [
    path("", include(router.urls)),
]