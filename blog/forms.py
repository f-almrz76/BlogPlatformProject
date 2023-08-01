from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "author")


class CommentUpdateForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())
