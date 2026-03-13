
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
       
            # name = validated_data['name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data.pop('password')
            user = User.objects.create_user(**validated_data)
            user.set_password(password)
            user.save()
        
            
       
            return user
        
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only = True) 
    password = serializers.CharField(write_only = True)  
    
    def validate(self, attrs):
         user = authenticate(username=attrs['username'], password=attrs['password'])
         
         if not user:
             raise serializers.ValidationError("Invalid credentials")
         attrs['user'] = user
         return user     