from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]


def index(request):
    posts = Post.objects.order_by('-creation_date')
    return render(request, 'posts/index.html', {'posts': posts})


@login_required
def add_post(request):
    form = AddPostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponse('done')

    return render(request, 'posts/new.html', {'form': form})
