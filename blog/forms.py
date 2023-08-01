from django import forms
from .models import Post
from users.models import Author


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category']


class CommentForm(forms.Form):

    CHOICES = [(author.id, author.name) for author in Author.objects.all()]

    post = forms.IntegerField()
    author = forms.TypedChoiceField(choices=CHOICES)
    content = models.TextField()


