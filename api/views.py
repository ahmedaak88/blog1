from django.shortcuts import render
from rest_framework.generics import ListAPIView , RetrieveAPIView , DestroyAPIView , CreateAPIView , RetrieveUpdateAPIView
from post.models import Post 
from .serializers import PostListSerializers ,PostDetailSerializers ,PostCreateSerializers

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializers
class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializers
	lookup_field = 'slug'
	lookup_url_kwarg = 'post_slug'
class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializers
	lookup_field = 'slug'
	lookup_url_kwarg = 'post_slug'

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateSerializers

	def perform_create(self,serializer):
		serializer.save(author=self.request.user)
class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializers
    lookup_field = 'slug'
    lookup_url_kwarg = 'post_slug'
