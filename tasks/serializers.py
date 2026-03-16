from .models import Task
from  datetime import datetime
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["author"]
       
    def validate_due_date(self, value):
        
        if value <= datetime.now():
            serializers.ValidationError("Error:Due date should be in the future")
            
        return value    
     
    
        
           
        