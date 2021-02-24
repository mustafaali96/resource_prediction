from django.urls import path, include

from webapp.views.training import views

urlpatterns = [
    path("post/", views.PostTrainingAPIListView.as_view())
]