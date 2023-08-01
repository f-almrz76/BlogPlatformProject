from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


# Create your views here.


def author_list(request):
    all_author = Author.objects.all()
    return render(request, "Author/authors.html", {"all_author": all_author})


def author_details(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, "Author/author.html", {"author": author})

def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "Blog/post_list.html", {"all_posts": all_posts})


def onepost(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "BLog/post.html", {"post": post})

def category_details(request, pk):
    categories = Category.objects.get(id=pk)
    return render(request, "Blog/category_details.html", {"category": categories})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_details')
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, 'Blog/post.html', context)

def comment(request):
    all_comments = Comment.objects.all()
    return render(request, "Comment/comment_list.html", {"all_comments": all_comments})

def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.content = form.cleaned_data['content']
            comment.save()
            return redirect('onepost', post_id=comment.post.id)
    else:
        form = CommentForm(initial={'content': comment.content})
    
    context = {'form': form}
    return render(request, 'update_comment.html', context)