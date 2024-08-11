from .import views
from django.urls import path

urlpatterns = [
    path('register/',views.RegisterAPIView.as_view(),name='register_view'),
    path('login/',views.LoginAPIView.as_view(),name='login_view')
]
