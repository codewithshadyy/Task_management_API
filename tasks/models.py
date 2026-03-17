from django.db import models
from django.utils import timezone

from django.conf import settings

class Task(models.Model):
    PRIORITY_LEVEL = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high')
    ]
    
    TASK_STATUS = [
        ("pending", "pending"),
        ("completed", "compleleted")
    ]
    title = models.CharField()
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks")
    due_date = models.DateTimeField(auto_now_add=True)
    priority_level = models.CharField(choices=PRIORITY_LEVEL, default='medium')
    status = models.CharField(choices=TASK_STATUS, default='pending')
    completed_at = models.DateTimeField(blank=True, null=True)
    
    def mark_complete(self):
        self.status = "completed",
        self.completed_at = timezone.now()
        self.save()
        
    def mark_incomplete(self):
        self.status = "pending",
        self.completed_at = None
        self.save()
            
    
    def __str__(self):
        return self.title
