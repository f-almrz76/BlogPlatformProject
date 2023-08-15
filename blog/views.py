from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Comment
from users.models import Author
from .forms import *
from django.views.generic import ListView,DetailView,UpdateView


# Create your views here.
class PostDetailView(DetailView):
    model = Post
    template_name = "Blog/post.html"
    context_object_name = "post"
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comment_set.all()
        context["comments"] = comments
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment = request.POST.get('comm')
        author_name = request.POST.get('username')
        
        if comment and author_name:
            author, created = Author.objects.get_or_create(name=author_name)
            Comment.objects.create(post=post, author=author, content=comment)
        
        return redirect('post_details', pk=post.pk)
    

# def post_details(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comment_set.all()
#     if request.method == 'POST':
#         comment = request.POST.get('comment')
#         author = request.POST.get('username')
#         if comment != None and author != None:
#             if Author.objects.filter(name=author).exists():
#                 Comment.objects.create(post=post, author=author, content=comment)
#             else:
#                 author = Author.objects.create(name=author)
#                 Comment.objects.create(post=post, author=author, content=comment)
#             return redirect('post_details', pk)

#     return render(request, "Blog/post.html", {"post": post, "comments": comments})

def home(request):
    context = {}
    if request.GET.get('search'):
        search = request.GET['search']
        cd = Post.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))
        context = {'searched': cd}

    return render(request, 'index.html', context)


def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "Blog/post_list.html", {"all_posts": all_posts})




def category_list(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Category.objects.create(name=name, description=description)

    all_category = Category.objects.all()

    return render(request, "Blog/category_list.html", {"all_category": all_category})


def category_details(request, pk):
    if request.method == 'POST':
        form=ModelForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Post.objects.create(title=cd['title'], content=cd['content'], publication_date=cd['publication_date'],
                                category=cd['category'], author=cd['author'])
    else:
        category = Category.objects.get(id=pk)
        authors = Author.objects.all()
        posts = category.post_set.all()
    return render(request, "Blog/category_details.html",
                  {"category": category, 'posts': posts, 'authors': authors})

# def update_comment(request):
#     if request.method=="POST":
#         comment=CommentForm(request.POST)
#         if comment.is_valid():
#             cd=comment.cleaned_data
#             Comment.objects.create(content=cd['content'])
#     else:
#         form=CommentForm()
#     return render(request, '"Blog/commnet_update.html"', {'form': form})

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'Blog/comment_update.html'

    def form_valid(self, form):
        return super().form_valid(form)
    