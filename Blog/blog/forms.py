from django import forms
from .models import Post
from users.models import Author


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']


class CommentUpdateForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)


class CommentCreationForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    content = forms.CharField(widget=forms.Textarea)