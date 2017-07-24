from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)

	def __str__(self):
		return self.title

	def get_absoulute_url(self):
		return reverse("post:detail", kwargs={"post_id": self.id})
	def name_val(self):
		return str(self.id) 
		pass