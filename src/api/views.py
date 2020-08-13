from django.shortcuts import render
from lists import models
from . import serializers
from rest_framework import generics

class ListToDo(generics.ListCreateAPIView):
    queryset = models.list.objects.all()
    serializer_class = serializers.ListSerializer

class DetailToDo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.list.objects.all()
    serializer_class =serializers.ListSerializer



