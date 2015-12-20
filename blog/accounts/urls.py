from django.conf.urls import url, include
from django.core.urlresolvers import reverse_lazy
from .views import SignUpView, signup_ok

urlpatterns = [

    url(r'^', include('registration.backends.hmac.urls')),

    # signup
    url(r'^signup/$', SignUpView.as_view(success_url=reverse_lazy('signup-ok')), name='signup'),
    url(r'^signup/done/$', signup_ok, name='signup-ok'),

    # login
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
]
