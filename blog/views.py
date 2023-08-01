from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Comment
from users.models import Author
from .forms import PostForm


# Create your views here.


def home(request):
    context = {}
    if request.GET.get('search'):
        search = request.GET['search']
        cd = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
        id=request.session["last_seen_post_id"]
        author_id=request.session["last_seen_post_author"]
        title=request.session["last_seen_post_title"]
        context = {'searched': cd,"id":id,"author_id":author_id,"title":title}

    return render(request, 'index.html', context)


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "Blog/post_list.html", {"all_posts": all_posts})


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.all()
    if request.method == 'POST':
        comment = request.POST.get('comment')
        author = request.POST.get('username')
        if comment != None and author != None:
            if Author.objects.filter(name=author).exists():
                Comment.objects.create(post=post, author=author, content=comment)
            else:
                author = Author.objects.create(name=author)
                Comment.objects.create(post=post, author=author, content=comment)
            return redirect('post_details', pk)

    request.session["last_seen_post_id"] = post.id
    request.session["last_seen_post_author"] = post.author.id
    request.session["last_seen_post_title"] = post.title
    return render(request, "Blog/post.html", {"post": post, "comments": comments})


def category_list(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Category.objects.create(name=name, description=description)

    all_category = Category.objects.all()

    return render(request, "Blog/category_list.html", {"all_category": all_category})


def category_details(request, pk):

    if request.method == 'POST':

        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title=cd["title"]
            content= cd["content"]
            author=cd["author"]
            category=Category.objects.get(id=pk)
            authors = Author.objects.all()
            posts = category.post_set.all()
            Post.objects.create(title=title,content=content,category=category ,author=author)
    else:
        category = Category.objects.get(id=pk)
        authors = Author.objects.all()
        posts = category.post_set.all()
        form = PostForm()
    return render(request, "Blog/category_details.html",
                  {"category": category, 'posts': posts, 'authors': authors,"form":form})
