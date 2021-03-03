from django.urls import path, include

from webapp.views.project import views

urlpatterns = [
    path("post/", views.PostProjectAPIListView.as_view())
]