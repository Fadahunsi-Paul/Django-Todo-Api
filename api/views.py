from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TodoApiView(APIView):
    def get(self,request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo)
        return Response(serializer,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = TodoSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class TodoListView(APIView):
    def get(self,request,id):
        try:
            todo = Todo.objects.all(id=id)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo)
        return Response(serializer,status=status.HTTP_200_OK) 
    
    def put(self,request,id):
        todo = 
        serializer = TodoSerializer