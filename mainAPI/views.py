from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuItemSerializer
from .models import MenuItem
# Create your views here.
class AllMenuItems(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer

