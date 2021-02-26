from django.urls import path, include
from rest_framework.routers import DefaultRouter

from webapp.views.modules import views

router = DefaultRouter()
router.register("update", views.UpdateModuleView)

urlpatterns = [
    path("get/", views.GetAllModulesAPIListView.as_view()),
    path("byTemplate/<template_id>/", views.GetAllModulesByTemplateAPIView.as_view()),
    path("", include(router.urls))

]