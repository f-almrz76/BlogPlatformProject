from django import forms
from django.forms import ModelForm
from .models import Comment

class CommentForm(forms.Form):
   content = forms.TextField()