from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['user','title','description','status','created_at']
        read_only_fields = ['updated_at','created_at']
