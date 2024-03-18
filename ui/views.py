from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *

# Create your views here.

class HomePage(ListView):

	model = Blog
	template_name = "home/home.html"
	context_object_name = "blog"

	def  get_queryset(self):

		blog = Blog.objects.all().order_by('-created_at')
		return blog;

class BlogDetail(DetailView):

	model = Blog
	template_name = "blog/blog-detail.html"
	context_object_name = "blogDetail"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		slug = self.kwargs.get('slug')
		context['blogRelated'] = Blog.objects.exclude(id=slug)[:3]
		return context

	def get_object(self, **kwargs):
		slug = self.kwargs.get('slug')
		blog = Blog.objects.filter(id=slug).first()
		return blog


	

