from django.urls import path
from dashboard import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/<name>", views.dashboarder, name="dashboarder"),
]
