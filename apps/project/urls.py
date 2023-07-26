from django.urls import path
from apps.project.views import (
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectListView,
)

app_name = "project"

urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("create/", ProjectCreateView.as_view(), name="project_create"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
    path("<int:pk>/update/", ProjectUpdateView.as_view(), name="project_update"),
    path("<int:pk>/delete/", ProjectDeleteView.as_view(), name="project_delete"),
]
