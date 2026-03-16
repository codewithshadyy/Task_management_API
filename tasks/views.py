from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from .permissions import ISAuthorOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    authentication_classes = [IsAuthenticated, ISAuthorOnly]
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    

