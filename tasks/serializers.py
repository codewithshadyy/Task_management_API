from .models import Task
from  datetime import datetime
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["author", "completed_at"]
       
    def validate_due_date(self, value):
        
        if value <= datetime.now():
            serializers.ValidationError("Error:Due date should be in the future")
            
        return value 
    
    # a function to prevent edits if task is completed
    
    def update(self, instance, validated_data):
        if instance.status == "completed"  and validated_data.get("status") != "pending":
            
            raise serializers.ValidationError("Sorry completed task cannot be editted")
        return super().update(instance, validated_data)      
     
    
        
           
        