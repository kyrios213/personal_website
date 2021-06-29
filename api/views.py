from django.shortcuts import render
from rest_framework import generics

from .models import Profile, Projects
from .serializers import ProjectsSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
