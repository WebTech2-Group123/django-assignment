from django import forms
from .models import Post


# new post form
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]
