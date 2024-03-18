from django.contrib import admin
from .models import *


class BlogModelAdmin(admin.ModelAdmin):

	readonly_fields = ['created_at']

	def get_readonly_fields(self, request, obj=None):
		if obj and obj.user != request.user:
			return [field.name for field in obj._meta.fields]
		return self.readonly_fields

# Register your models here.
admin.site.register(Blog, BlogModelAdmin)
