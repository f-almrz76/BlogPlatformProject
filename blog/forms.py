from django import forms
from .models import Post,Author

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentUpdateForm(forms.Form):
    content = forms.CharField()