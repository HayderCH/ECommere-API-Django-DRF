from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class CategoryView(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
