from django.urls import path, include

from webapp.views.platform import views

urlpatterns = [
    path("get/", views.GetPlatformAPIListView.as_view())
]
