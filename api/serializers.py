from rest_framework import serializers
from post.models import Post 

class PostListSerializers(serializers.ModelSerializer):
	class Meta:
		model = Post 
		fields = ['title','author','slug','content','publish']


class PostDetailSerializers(serializers.ModelSerializer):
	class Meta:
		model = Post 
		fields = ['title','author','slug','content','publish','draft','id']


class PostCreateSerializers(serializers.ModelSerializer):
	class Meta:
		model = Post 
		fields = ['title','content','draft','publish']

