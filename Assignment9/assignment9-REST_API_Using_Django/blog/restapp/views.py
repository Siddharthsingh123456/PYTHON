from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from restapp.serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from restapp.models import BlogPost
from restapp.permissions import IsPostPossessor
from restapp.filters import PostFilter

# Create your views here.

class RestAPPView(APIView):

    def get(self,request):
        return Response({'message':'Hello world!'})

class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PostFilter
    ordering_fields = ['id']
    search_fields = ['title', 'content']

    def get_queryset(self):
        return BlogPost.objects.filter(created_by=self.request.user)