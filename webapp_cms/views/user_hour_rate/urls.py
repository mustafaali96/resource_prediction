from django.urls import path, include

from webapp_cms.views.user_hour_rate import views

urlpatterns = [
    path("", views.UserRate.as_view(), name="user_rate"),
]