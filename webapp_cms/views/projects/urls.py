from django.urls import path, include

from webapp_cms.views.projects import views

urlpatterns = [
    path("", views.ProjectView.as_view(), name="all_projects"),
    # path("edit/<project_id>", views.EditBadge.as_view(), name="show_project_details"),
]