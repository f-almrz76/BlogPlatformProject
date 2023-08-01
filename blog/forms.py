from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


class UpdateCommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
