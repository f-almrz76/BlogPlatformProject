from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from users.models import Author
from django.http import HttpResponse
from .forms import PostForm

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
