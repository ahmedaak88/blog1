from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 




class Post(models.Model):
	author = models.ForeignKey(User, default=1)
	title = models.CharField(max_length=255)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)
	image = models.ImageField(upload_to="blog_images", null=True , blank=True)
	slug = models.SlugField(unique=True, null=True)
	draft  = models.BooleanField(default=True)
	publish= models.DateField()

	def __str__(self):
		return self.title

	def get_absoulute_url(self):
		return reverse("post:detail", kwargs={"slug": self.slug})
	def update_url_post(self):
		return reverse("post:update", kwargs={"slug": self.slug})
	def delete_url(self):
		return reverse("post:delete", kwargs={"slug": self.slug})
	def create_url(self):
		return redirect("post:create")
	def croping(self):
		return str(self.content[0:30])
		pass
	def name_val(self):
		return str(self.id) 
		pass
	class Meta:
		ordering= ['-timestamp', '-updated']




def post_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		slug=slugify(instance.title)
		qs= Post.objects.filter(slug=slug).order_by("-id")
		if qs.exists():
			slug= "%s-%s"%(slug , instance.id)
		instance.slug = slug 
		instance.save()

post_save.connect(post_reciever,sender=Post)

class Like(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	
