from rest_framework import viewsets

from .serializers import PostSerializer
from news.models import Post
from django.db import models
from django.contrib.auth import get_user_model

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    