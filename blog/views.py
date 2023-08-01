from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Comment
from .forms import UpdateCommentForm
from users.models import Author


# Create your views here.


def home(request):
    context = {}
    user = request.user
    if request.session.get[user.pk]:
        post = request.session.get[user.pk]["last_seen_post"]
    else:
        post = None
    if request.GET.get("search"):
        search = request.GET["search"]
        cd = Post.objects.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        )
        context = {"searched": cd, "post": post}

    return render(request, "index.html", context)


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "Blog/post_list.html", {"all_posts": all_posts})


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.all()
    user = request.user
    request.session[user.pk] = {"last_seen_post": post}
    request.session.modified = True
    if request.method == "POST":
        comment = request.POST.get("comment")
        author = request.POST.get("username")
        if comment != None and author != None:
            if Author.objects.filter(name=author).exists():
                Comment.objects.create(post=post, author=author, content=comment)
            else:
                author = Author.objects.create(name=author)
                Comment.objects.create(post=post, author=author, content=comment)
            return redirect("post_details", pk)

    return render(request, "Blog/post.html", {"post": post, "comments": comments})


def category_list(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        Category.objects.create(name=name, description=description)

    all_category = Category.objects.all()

    return render(request, "Blog/category_list.html", {"all_category": all_category})


def category_details(request, pk):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        Category.objects.create(name=name, description=description)
        return redirect("category_details", pk)

    else:
        category = Category.objects.get(id=pk)
        authors = Author.objects.all()
        posts = category.post_set.all()
    return render(
        request,
        "Blog/category_details.html",
        {"category": category, "posts": posts, "authors": authors},
    )


def update_comment(request, pk):
    if request.method == "POST":
        comment = Comment.objects.get(pk=pk)
        form = UpdateCommentForm(request.POST, isinstance=comment)
        if form.is_valid():
            form.save()
        return redirect("update_comment", pk, {"form": form})

    else:
        form = UpdateCommentForm()
    return render(
        request,
        "Blog/update_comment.html",
        {"form": form},
    )


def author_details(request, pk):
    author = Author.objects.get(pk=pk)
    return render(
        request,
        "Blog/category_details.html",
        {"author": author},
    )
