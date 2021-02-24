from django.urls import path, include

from webapp.views.modules import views

urlpatterns = [
    path("get/", views.GetAllModulesAPIListView.as_view()),
    path("byTemplate/<template_id>/", views.GetAllModulesByTemplateAPIView.as_view())
]
