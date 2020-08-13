from django.urls import path,include

from .import views

urlpatterns = [
    path('',views.ListToDo.as_view()),
    path('<int:pk>/', views.DetailToDo.as_view()),
    path('rest-auth/',include('rest_auth.urls')),
]