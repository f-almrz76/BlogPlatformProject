from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.


def author_list(request):
    all_author = Author.objects.all()
    return render(request, "Author/authors.html", {"all_author": all_author})


def author_details(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, "Author/author.html", {"author": author})

def category_detailes(request, pk):
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
    return render(request, 'post.html', context)