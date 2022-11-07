from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseBadRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Tag
from .serializer import TagSerializer
from rest_framework import status

from rest_framework import generics

# Create your views here.
class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailAPIView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer