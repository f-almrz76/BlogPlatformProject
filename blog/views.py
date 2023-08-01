from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Post, Comment
from users.models import Author
from django.http import HttpResponse
from .form import CategoryForm, PostForm

# Create your views here.


def home(request):
    query = request.GET.get('q')
    author = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'template/index.html', {'author': author})


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

def category_list(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'category_list.html', {'categories': categories, 'form': form})

def category_details(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.category = category
            post.save()
            return redirect('category_details', category_id=category_id)
    else:
        form = PostForm()

    return render(request, 'category_details.html', {'category': category, 'posts': posts, 'form': form})


def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    # Save the ID of the last seen post in the session
    request.session['last_post_id'] = post_id

    return render(request, 'post_details.html', {'post': post})


def index(request):
    last_post_id = request.session.get('last_post_id')

    last_post = get_object_or_404(Post, pk=last_post_id) if last_post_id else None

    latest_posts = Post.objects.order_by('-created_at')[:5]

    return render(request, 'index.html', {'last_post': last_post, 'latest_posts': latest_posts})