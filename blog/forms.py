from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "author"]


class UpdateCommentForm(forms.Form):
    content = forms.TextInput()