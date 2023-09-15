from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.
# class AllMenuItems(generics.ListCreateAPIView):
#     queryset=MenuItem.objects.select_related("category").all()
#     serializer_class=MenuItemSerializer
    
# class SingleMenuItem(generics.RetrieveAPIView,generics.DestroyAPIView):
#     queryset=MenuItem.objects.select_related("category").all()
#     serializer_class=MenuItemSerializer
@api_view(['GET','POST'])
def AllMenuItems(request):
    if request.method=='GET':
        items=MenuItem.objects.select_related("category").all()
        category_name=request.query_params.get('category')
        to_price=request.query_params.get('to_price')
        if category_name:
            items=items.filter(category__slug__istartswith=category_name)
        if to_price:
            items=items.filter(price=to_price)
        serialized_items=MenuItemSerializer(items,many=True)
        return Response(serialized_items.data,status=status.HTTP_200_OK)
    if request.method=='POST':
        serialized_item=MenuItemSerializer(request.data,many=True)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data,status=status.HTTP_201_CREATED)

@api_view()
#@renderer_classes([TemplateHTMLRenderer])
def SingleMenuItem(request,pk):
    item=MenuItem.objects.select_related("category").get(pk=pk)
    serialized_items=MenuItemSerializer(item)
    return Response(serialized_items.data)
@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data':serialized_item.data}, template_name='menu_item.html')

# class AllMenuItems(APIView):
#     def get(self,request):
#         items=MenuItem.objects.select_related("category").all()
#         serializer=MenuItemSerializer(items,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         serialized_item=MenuItemSerializer(data=request.data)
#         serialized_item.is_valid(raise_exception=True)
#         serialized_item.save()
    
# class SingleMenuItem(APIView):
#     def get(self, request, pk):
#         try:
#             item = MenuItem.objects.select_related("category").get(pk=pk)
#             serializer = MenuItemSerializer(item)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except MenuItem.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)