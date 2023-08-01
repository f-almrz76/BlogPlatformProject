from django.forms import ModelForm
from .models import Post
from django.forms import forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ["publication_date", "author"]


class UpdateComment(forms.Form):
    