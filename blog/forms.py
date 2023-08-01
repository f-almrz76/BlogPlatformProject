from django import forms
from .models import Post,Author

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentUpdateForm(forms.Form):
    post = forms.ForeignKey(Post, on_delete=forms.CASCADE)
    author = forms.ForeignKey(Author, on_delete=forms.CASCADE)
    content = forms.CharField()
    comment_date = forms.DateField(auto_now_add=True)