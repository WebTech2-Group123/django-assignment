from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Post
from .forms import AddPostForm


# posts list -> return all post in reverse chronological order
def index(request):
    posts = Post.objects.order_by('-creation_date')
    return render(request, 'posts/index.html', {'posts': posts})


# add a new post
@login_required
def add_post(request):
    form = AddPostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('posts:index')

    return render(request, 'posts/new.html', {'form': form})
