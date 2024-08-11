from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TodoApiView(APIView):
    def get(self,request):
        serializer = TodoSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self):
        