from django.conf.urls import url
from . import views

urlpatterns = [

    # posts list
    url(r'^$', views.index, name='index'),

    # new post
    url(r'^new$', views.add_post, name='new'),
]
