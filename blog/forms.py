from django import forms
from .models import Category, Post
from users.models import Author


class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    author = forms.ModelChoiceField(queryset=Author.objects.all())

    def save(self):
        cd = self.cleaned_data
        post = Post(title=cd['title'], content=cd['content'], category=cd['category'], author=cd['author'])
        post.save()
        return post