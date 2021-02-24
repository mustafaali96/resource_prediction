from django.urls import path, include

from webapp.views.prediction import views

urlpatterns = [
    path("post/", views.GetPredictionAPIListView.as_view())
]