from django import forms
from .models import Post
class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'publication_date')
        