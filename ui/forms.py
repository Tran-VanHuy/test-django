from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class BlogForm(forms.ModelForm):

	class Meta:
		model = Blog
		fields = "__all__"

	title = forms.CharField(
		required = True,
		widget=forms.TextInput(
			attrs={
			'type': 'text',
			'class': 'input rounded px-4 mb-3 py-2',
			'placeholder': 'Title blog *',

			}
			)
		)
	short_content = forms.CharField(
		required = True,
		widget=forms.Textarea(
			attrs={
			'type': 'text',
			'class': 'input short-content-input rounded px-4 mb-3 py-2',
			'placeholder': 'Short content blog *'
			}
			)
		)
	content = forms.CharField(
		required = True,
		widget=forms.Textarea(
			attrs={
			'type': 'text',
			'class': 'input rounded px-4 mb-3 py-2',
			'placeholder': 'Content blog *'
			}
			)
		)

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'rounded border-0 mb-3 p-2 w-100 input-login w-100 text-main'
			field.widget.attrs['placeholder'] = field.label