from django.conf.urls import url, include
from .views import profile

urlpatterns = [

    # login
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),

    # logout
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),

    # profile
    url(r'^profile/$', profile, name='profile'),

    # registration, activation
    url(r'^', include('registration.backends.hmac.urls')),

]
