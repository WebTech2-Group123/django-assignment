from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import generic
from django.shortcuts import render


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'accounts/signup.html'


def signup_ok(request):
    return render(request, 'accounts/signup_ok.html')
