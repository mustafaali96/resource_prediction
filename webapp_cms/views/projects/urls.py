from django.urls import path, include

from webapp_cms.views.projects import views

urlpatterns = [
    path("", views.ProjectView.as_view(), name="all_projects"),
    path("project/<p_id>", views.ProjectPredictionView.as_view(), name="project_prediction"),
]