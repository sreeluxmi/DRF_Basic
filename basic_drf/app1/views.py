from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product


# Create your views here.

class ApiOverview(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        api_urls = {
            'List': '/product-list',
            'Create': '/create-list',
            'Detail': '/product-detail/<int:id>',
            'Update': '/update/<int:id>',
            'Delete': '/delete/<int:id>'
        }
        return Response(api_urls)


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ProductUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ProductDelete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
