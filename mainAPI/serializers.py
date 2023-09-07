from rest_framework import serializers
from .models import MenuItem,Category
from decimal import Decimal
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","title","slug"]
       
    
class MenuItemSerializer(serializers.ModelSerializer):
    price_after_tax=serializers.SerializerMethodField(method_name="calculate_tax")
    category=CategorySerializer()
    class Meta:
        model=MenuItem
        fields=["id","title","inventory","price","price_after_tax","category"]
    
    def calculate_tax(self,product:MenuItem):
        return product.price*Decimal(1.5)