from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())