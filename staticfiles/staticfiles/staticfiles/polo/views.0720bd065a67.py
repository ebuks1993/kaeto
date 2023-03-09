from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer,CategorySerializer
from .models import category,products



class ProductViewset(ModelViewSet):
    queryset=products.objects.all()
    serializer_class=ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset=category.objects.all()
    serializer_class=CategorySerializer




