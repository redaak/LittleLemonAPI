from rest_framework import serializers
from .models import MenuItem,Category
from decimal import Decimal
import bleach
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","title","slug"]
        extra_kwargs={
            'price':{'min_value':2}
        }
    
class MenuItemSerializer(serializers.ModelSerializer):
    price_after_tax=serializers.SerializerMethodField(method_name="calculate_tax")
    category=CategorySerializer(read_only=True)
    def validate(self, attrs):
        attrs['title']=bleach.clean(attrs['title'])
        if (attrs['price']<2):
            raise serializers.ValidationError('price must be greater than or equal to 2')
        if (attrs['inventory']<0):
            raise serializers.ValidationError('inventory can not be a negative must be greater or equal to 0')
        return super().validate(attrs)
    class Meta:
        model=MenuItem
        fields=["id","title","inventory","price","price_after_tax","category"]
    
    def calculate_tax(self,product:MenuItem):
        return product.price*Decimal(1.5)
    