from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ProjectListView.as_view(), name="project_list"),
]
