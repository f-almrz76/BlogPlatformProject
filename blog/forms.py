from django import forms
from .models import Post


from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['content']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('post_details')