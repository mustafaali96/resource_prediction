from django.urls import path, include

from webapp.views.region import views

urlpatterns = [
    path("get/", views.GetRegionAPIListView.as_view())
]
