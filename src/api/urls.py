from django.urls import path,include

from .import views
from rest_framework import routers




urlpatterns = [
    path('',views.todo.as_view()),
    path('<int:pk>/', views.DetailToDo.as_view()),
    path('rest-auth/',include('rest_auth.urls')),
]