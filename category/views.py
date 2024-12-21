from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializer import CategorySerializer, CategoryCreateUpdateSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CategoryCreateUpdateSerializer
        return CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateUpdateSerializer
