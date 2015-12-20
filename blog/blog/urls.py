from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [

    # home
    url(r'^$', RedirectView.as_view(url=reverse_lazy('posts:index')), name='index'),

    # posts app
    url(r'^posts/', include('posts.urls', namespace='posts')),

    # accounts (login etc)
    url(r'^accounts/', include('accounts.urls')),

    # admin panel
    url(r'^admin/', admin.site.urls),

]
