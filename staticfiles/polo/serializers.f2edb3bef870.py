from rest_framework import serializers
from .models import category,products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields=['id','Title']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields=['id','Title',"Product"]