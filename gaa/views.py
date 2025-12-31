from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from .models import UserProfile

def landing(request):
    return render(request, 'landing.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            UserProfile.objects.create(
                user=user,
                favorite_club=form.cleaned_data['favorite_club']
            )

            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard(request):
    profile = request.user.userprofile
    return render(request, 'dashboard.html', {
        'user': request.user,
        'club': profile.favorite_club
    })
