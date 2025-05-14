from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def patch(self, request, *args, **kwargs):
        # Garantir que só 'title' e 'content' sejam atualizados
        partial = kwargs.pop('partial', True)
        instance = self.get_object()

        # Somente 'title' e 'content' do request.data
        data = {k: v for k, v in request.data.items() if k in ['title', 'content']}
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
