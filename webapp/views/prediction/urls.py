from django.urls import path, include

from webapp.views.prediction import views

urlpatterns = [
    path("post/", views.PostPredictionAPIListView.as_view())
]