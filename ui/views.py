from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from . import forms
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

# Create your views here.
User = get_user_model()

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

class UpdateBlog(LoginRequiredMixin, TemplateView):
	template_name = "blog/update-blog.html"
	form_class = forms.BlogForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = self.form_class()
		context['blog'] = Blog.objects.all().order_by('-created_at')
		return context

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		form = self.form_class(self.request.POST, request.FILES)
		if request.POST.get('form_type') == "create":
			if form.is_valid():
				blog = form.save(commit=False)
				blog.user = request.user
				blog.save()
			else:
				context['form'] = form

		if request.POST.get('form_type') == "delete":
			id = request.POST.get('id_blog')
			blogDetail = Blog.objects.filter(id=id).first()
			if request.user == blogDetail.user:
				blogDetail.delete()
				context['message'] = "Delete success"
			else:
				context['message'] = "Do not have permission to delete"

		if request.POST.get('form_type') == "edit-submit":
			id = request.POST.get('id')
			blogDetail = Blog.objects.filter(id=id).first()
			if request.user == blogDetail.user:
				if form.is_valid():
					blog = form.save(commit=False)
					blogDetail.image = form.cleaned_data['image']
					blogDetail.title = form.cleaned_data['title'] 
					blogDetail.short_content = form.cleaned_data['short_content']
					blogDetail.content = form.cleaned_data['content']
					blogDetail.user = request.user
					blogDetail.save()
					context['message'] = "update success"
				else:
					context['message'] = "update fail"
			else:
				context['message'] = "do not have permission to update"
		return self.render_to_response(context)

def UpdateBlogApi(request, id):
	if request.method == "GET":
		try:
			blogDetail = Blog.objects.filter(id=id).first()
			if blogDetail is not None:
				blog_data = {
                    "id": blogDetail.id,
                    "image": blogDetail.image.url,
                    "title": blogDetail.title,
                    "short_content": blogDetail.short_content,
                    "content": blogDetail.content
                }
				return JsonResponse({'context': blog_data})
		except Exception as e:
			return HttpResponseBadRequest({'Invalid request',e })
	return HttpResponseBadRequest('Invalid request 1')
	
class Login(LoginView):
	form_class = forms.LoginForm
	template_name = "login/login.html"

	def get_success_url(self):
		return reverse_lazy('update-blog')

class Logout(LogoutView):
	def get_success_url(self):
		return reverse_lazy('home-page')
	



	

