from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from users.models import Author
from django.http import HttpResponse
from .forms import PostForm, CommentForm

# Create your views here.


def home(request):
    context = {}
    return render(request, 'index.html', context)


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "Blog/post_list.html", {"all_posts": all_posts})


def post_details(request, pk):
    context = {}
    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        context = {"post": post}
    return render(request, "Blog/post.html", context)


def category_list(request):
    all_category = Category.objects.all()
    return render(request, "Blog/category_list.html", {"all_category": all_category})


def category_details(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "Blog/category_details.html", {"category": category })


def category_view(request):
    context = {}

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        form.save()

    context['form'] = form
    return render(request, "category_details.html", context)


def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    request.session['last_post_id'] = post_id
    return render(request, 'post.html', {'post': post})


def show_last_post(request):
    last_post_id = request.session.get('last_post_id')
    last_post = Post.objects.get(id=last_post_id)
    return render(request, 'dashboard.html', {'last_post': last_post})


def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.content = form.cleaned_data['content']
            comment.save()
            return redirect('post_detail', comment_id=comment.id)

    return render(request, 'post_detail.html', {'form': form})
