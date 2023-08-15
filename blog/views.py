from typing import Any, Dict
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Comment
from users.models import Author
from .forms import PostCreationForm, CommentUpdateForm, CommentCreationForm
from django.http import HttpResponse
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    context = {}
    if request.GET.get("search"):
        search = request.GET["search"]
        cd = Post.objects.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        )
        context = {"searched": cd}

    return render(request, "index.html", context)


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "Blog/post_list.html", {"all_posts": all_posts})


class PostDetailsView(DetailView):
    model = Post
    template_name = "Blog/post.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = post.comment_set.all()

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment = request.POST.get("comm")
        author = request.POST.get("username")
        if comment != None and author != None:
            if Author.objects.filter(name=author).exists():
                Comment.objects.create(post=post, author=author, content=comment)
            else:
                author = Author.objects.create(name=author)
                Comment.objects.create(post=post, author=author, content=comment)
            return redirect("post_details", kwargs["pk"])


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentUpdateForm
    template_name = "Blog/comment_update.html"

    def get_success_url(self):
        return reverse_lazy("post_details", args=[self.object.post.id])



def category_list(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        Category.objects.create(name=name, description=description)

    all_category = Category.objects.all()

    return render(request, "Blog/category_list.html", {"all_category": all_category})


def category_details(request, pk):
    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid:
            f = form.save(commit=False)
            category = Category.objects.get(id=pk)
            f.category = category
            f.save()

        return redirect("blog:category_details", pk)
    else:
        form = PostCreationForm()
        category = Category.objects.get(id=pk)
        authors = Author.objects.all()
        posts = category.post_set.all()
    return render(
        request,
        "Blog/category_details.html",
        {"category": category, "posts": posts, "authors": authors, "form": form},
    )
