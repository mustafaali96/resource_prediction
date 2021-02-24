from django.urls import path, include

from webapp.views.template import views

urlpatterns = [
    path("get/", views.GetTemplateAPIListView.as_view())
]
