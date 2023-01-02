from rest_framework import serializers
from .models import *

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Items
        fields = '__all__'

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Suppliers
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'

