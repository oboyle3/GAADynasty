from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from .models import UserProfile, Author

def landing(request):
    authors = Author.objects.all()
    context = {
        'authors': authors,
    }
    return render(request, 'landing.html', context)


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
    season = Season.objects.filter(user=request.user).first()
    return render(request, 'dashboard.html', {
        'user': request.user,
        'club': profile.favorite_club,
        'season': season,
    })


from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Season, GAAClub

@login_required
def start_season(request):
    # Prevent duplicate seasons
    if Season.objects.filter(user=request.user).exists():
        return redirect("dashboard")

    # Example: first club or chosen club logic
    club = GAAClub.objects.first()  # replace with actual selection logic

    Season.objects.create(
        user=request.user,
        coached_club=club,
        offensive_style="BAL"  # or default value
    )

    return redirect("dashboard")


from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Season, GAAClub


@login_required
def start_season(request):
    # Don’t allow multiple seasons
    if Season.objects.filter(user=request.user).exists():
        return redirect("dashboard")

    # TEMP: assign first club (you can replace with chooser later)
    club = GAAClub.objects.first()

    Season.objects.create(
        user=request.user,
        coached_club=club,
        offensive_style="BAL"
    )

    return redirect("dashboard")





