from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm


# render the profile page
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


# render the profile edit form
@login_required
def profile_edit(request):
    form = ProfileEditForm(request.POST or None, instance=request.user)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'accounts/profile_edit.html', {'form': form})
