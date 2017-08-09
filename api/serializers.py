from rest_framework import serializers
from post.models import Post 



class PostListSerializers(serializers.ModelSerializer):
	author = serializers.SerializerMethodField()
	detail = serializers.HyperlinkedIdentityField(
		view_name="api:detail",
		lookup_field="slug",
		lookup_url_kwarg="post_slug"
		)
	class Meta:
		model = Post 
		fields = ['title','author','slug','content','publish','detail']
	def get_author(self,obj):
		return str(obj.author.username)


class PostDetailSerializers(serializers.ModelSerializer):
	author = serializers.SerializerMethodField()
	
	delete = serializers.HyperlinkedIdentityField(
		view_name="api:delete",
		lookup_field="slug",
		lookup_url_kwarg="post_slug"
		)

	update = serializers.HyperlinkedIdentityField(
		view_name="api:update",
		lookup_field="slug",
		lookup_url_kwarg="post_slug"
		)
	class Meta:
		model = Post 
		fields = ['id','title','author','slug','content','publish','draft','id' , 'delete' ,'update']

	def get_author(self,obj):
		return str(obj.author.username)
class PostCreateSerializers(serializers.ModelSerializer):
	class Meta:
		model = Post 
		fields = ['title','content','draft','publish']

