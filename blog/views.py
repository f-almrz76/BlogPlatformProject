from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Comment
from users.models import Author


# Create your views here.


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


def post_details(request, pk):
        post = get_object_or_404(Post, pk=pk)
        recently_viewed_tasks = None

        if 'recently_viewed' in request.session:
            if pk in request.session['recently_viewed']:
                request.session['recently_viewed'].remove(pk)

            posts = Post.objects.filter(pk__in = request.session['recently_viewed'])
            recently_viewed_tasks = sorted(posts,key = lambda x: request.session['recently_viewed'].index(x.pk))
            request.session['recently_viewed'].insert(0, pk)
            if len(request.session['recently_viewed']) > 5:
                request.session['recently_viewed'].pop()

        else:
            request.session['recently_viewed'] = [pk]
        
        request.session.modified = True


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

        return render(request, "Blog/post.html", {"post": post, "comments": comments,'recently_viewed_tasks':recently_viewed_tasks})


def category_list(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Category.objects.create(name=name, description=description)

    all_category = Category.objects.all()

    return render(request, "Blog/category_list.html", {"all_category": all_category})


def category_details(request, pk):
    if request.method == 'POST':
        pass
    else:
        category = Category.objects.get(id=pk)
        authors = Author.objects.all()
        posts = category.post_set.all()
    return render(request, "Blog/category_details.html",
                  {"category": category, 'posts': posts, 'authors': authors})
