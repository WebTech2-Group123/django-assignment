from django.conf.urls import url, include
from .views import profile, profile_edit

urlpatterns = [

    # login, logout, ecc. are already defined by Django

    # profile
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/edit$', profile_edit, name='profile_edit'),

    # registration, activation
    url(r'^', include('registration.backends.hmac.urls')),

]
