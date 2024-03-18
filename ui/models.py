from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
	image = models.FileField(upload_to="static/images", unique=True)
	title = models.CharField(max_length=255)
	short_content = models.CharField(max_length=255)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.title)
