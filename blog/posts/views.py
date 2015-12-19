from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post


def index(request):
    posts = Post.objects.order_by('-creation_date')
    return render(request, 'posts/index.html', {'posts': posts})


@login_required
def add_post(request):
    return HttpResponse('Add post')
