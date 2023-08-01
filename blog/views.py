from django.db.models import Q
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post, Category, Comment
from users.models import Author
from django.http import HttpResponse
from itertools import chain
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
    posts = Post.objects.filter(category=pk)
    form = PostForm()
    if request.method == 'GET':
        return render(request, "Blog/category_details.html", {"category": category , 'form': form, 'posts': posts})
    if request.method == 'POST':
        new_post = PostForm(request.post)
        if new_post.is_valid():
            new_post_model = new_post.save
        return render(request, "Blog/category_details.html", {"category": category , 'form': form, 'posts': posts})




def search_result(request):
    print(request)
    if request.method == 'POST':
        searched_content = request.POST['searched']
        posts1 = Post.objects.filter(title__contains=searched_content)
        posts2 = Post.objects.filter(content__contains=searched_content)
        results = list(chain(posts1 , posts2))
        # results = posts1
        print('results: ', results)
        return render(request, 'index.html', {'results': results})
    else:
        return render(request, 'index.html', {})
