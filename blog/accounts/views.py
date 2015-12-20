from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def profile_edit(request):
    form = ProfileEditForm(request.POST or None, instance=request.user)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'accounts/profile_edit.html', {'form': form})
