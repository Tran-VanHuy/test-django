from django.contrib import admin
from .models import *


class BlogModelAdmin(admin.ModelAdmin):

	readonly_fields = ['created_at']

	exclude = ['user']
	def has_change_permission(self, request, obj=None):
		if obj is not None and obj.user != request.user:
			return False
		return True

	def has_delete_permission(self, request, obj=None):
		if obj is not None and obj.user != request.user:
			return False
		return True

	def save_model(self, request, obj, form, change):
		if not obj.pk:
			obj.user = request.user 
		super().save_model(request, obj, form, change)

# Register your models here.
admin.site.register(Blog, BlogModelAdmin)
