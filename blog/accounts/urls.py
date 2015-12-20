from django.conf.urls import url, include

urlpatterns = [

    # login
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),

    # registration, activation
    url(r'^', include('registration.backends.hmac.urls')),

]
