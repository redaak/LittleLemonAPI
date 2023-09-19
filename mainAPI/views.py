from django.shortcuts import render
from rest_framework import generics
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.paginator import Paginator,EmptyPage
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
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
        search_name=request.query_params.get('search')
        ordering_by=request.query_params.get('orderby')
        perpage=request.query_params.get('perpage',default=2)
        page=request.query_params.get('page',default=1)
        if category_name:
            items=items.filter(category__slug__istartswith=category_name)
        if to_price:
            items=items.filter(price=to_price)
        if search_name:
            items=items.filter(category__title__istartswith=search_name)
        if ordering_by:
            ordering_fields=ordering_by.split(",")
            items=items.order_by(*ordering_fields)
        paginator=Paginator(items,per_page=perpage)
        try:
            items=paginator.page(number=page)
        except EmptyPage:
            items=[]
        serialized_items=MenuItemSerializer(items,many=True)
        if serialized_items.data:
            return Response(serialized_items.data,status=status.HTTP_200_OK)
        else:
            return Response(serialized_items.data,status=status.HTTP_404_NOT_FOUND)
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
@permission_classes([IsAuthenticated])
def secret(request):
    return Response('secret message')
@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def menu(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data':serialized_item.data}, template_name='menu_item.html')
@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    return Response('manager view')

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