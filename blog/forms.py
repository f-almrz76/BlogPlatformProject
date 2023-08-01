from .models import Post
from django import forms


class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = "__all__"
