from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from .permissions import ISAuthorOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import authentication
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, ISAuthorOnly]
  
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
    
    def perform_create(self, serializer):
         serializer.save(author=self.request.user)
         
    @action(detail=True, methods=["post"])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.mark_complete()
        return Response(TaskSerializer(task).data)
    @action(detail=True, methods=["post"])
    def mark_incomplete(self, request, pk=None):
        task = self.get_object()
        task.mark_incomplete()
        return Response(TaskSerializer(task).data)
    
             
         
      
    

