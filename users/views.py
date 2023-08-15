from django.shortcuts import render
from .models import Author


# Create your views here.

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.forms import CustomLoginForm


def login_view(request):

    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username']=username
                return redirect('home')
    else:
        form = CustomLoginForm()

    return render(request, 'Author/login.html', {'form': form })


def author_list(request):
    all_author = Author.objects.all()
    return render(request, "Author/authors.html", {"all_author": all_author})


def author_details(request, pk):
    author = Author.objects.get(id=pk)
    return render(request, "Author/author.html", {"author": author})