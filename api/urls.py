from django.urls import path
from .views import *

urlpatterns = [
    path('todo/',TodoApiView.as_view(),name='todo'),
    path('todo-list/',TodoListView.as_view(),name='todo-list')
]
