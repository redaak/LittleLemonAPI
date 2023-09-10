from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
# class AllMenuItems(generics.ListCreateAPIView):
#     queryset=MenuItem.objects.select_related("category").all()
#     serializer_class=MenuItemSerializer
    
# class SingleMenuItem(generics.RetrieveAPIView,generics.DestroyAPIView):
#     queryset=MenuItem.objects.select_related("category").all()
#     serializer_class=MenuItemSerializer
# @api_view()
# def AllMenuItems(request):
#     items=MenuItem.objects.select_related("category").all()
#     serialized_items=MenuItemSerializer(items,many=True)
#     return Response(serialized_items.data)

# @api_view()
# def SingleMenuItem(request):
#     item=MenuItem.objects.select_related("category").all()
#     serialized_items=MenuItemSerializer(item,many=True)
#     return Response(serialized_items.data)
class AllMenuItems(APIView):
    def get(self,request):
        items=MenuItem.objects.select_related("category").all()
        serializer=MenuItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serialized_item=MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
    
class SingleMenuItem(APIView):
    def get(self, request, pk):
        try:
            item = MenuItem.objects.select_related("category").get(pk=pk)
            serializer = MenuItemSerializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MenuItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)