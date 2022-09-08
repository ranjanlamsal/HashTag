from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Tag
from .serializer import TagSerializer
from rest_framework import status

# Create your views here.

class AllTagsAPI(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
            serializer = TagSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagAPI(APIView):
    def get(self, request, pk):
        tag = Tag.objects.get(id = pk)
        serializer = TagSerializer(tag)
        print(serializer.data)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
