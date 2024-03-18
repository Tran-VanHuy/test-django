from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here.

class HomePage(TemplateView):

	template_name = "home/home.html"

	def  get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		blog = Blog.objects.all()
		context["blog"] = blog

		return context;

class BlogDetail(TemplateView):

	template_name = "blog/blog-detail.html"

	def  get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		slug = self.kwargs['slug']

		blogDetail = Blog.objects.filter(id=slug).first()
		blogRelated = Blog.objects.exclude(id=slug)[0:3]

		context["blogDetail"] = blogDetail
		context["blogRelated"] = blogRelated
		return context;

