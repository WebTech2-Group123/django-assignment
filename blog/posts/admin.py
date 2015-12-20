from django.contrib import admin
from .models import Post

# register the Post model in the administration app
admin.site.register(Post)
