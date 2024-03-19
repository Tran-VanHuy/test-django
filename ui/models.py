from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
	image = models.FileField(upload_to="static/images", unique= True, null=True, blank=True)
	title = models.CharField(max_length=255, null=True, blank=True)
	short_content = models.CharField(max_length=255, null=True, blank=True)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return str(self.title)
