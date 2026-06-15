from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game


def home(request):
    return render(request, "home.html")

@login_required
def community(request):

    # ADD GAME
    if request.method == "POST":
        Game.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("desc"),
            image=request.FILES.get("img"),
            download_link=request.POST.get("link")
        )
        return redirect("community")

    # GET ALL GAMES
    games = Game.objects.all()

    # WELCOME MESSAGE (ONLY FIRST LOGIN AFTER SIGNUP)
    show_welcome = request.session.get("welcome", False)

    if show_welcome:
        del request.session["welcome"]

    # SINGLE RETURN (IMPORTANT)
    return render(request, "community.html", {
        "games": games,
        "show_welcome": show_welcome
    })


@login_required
def delete_game(request, game_id):
    Game.objects.get(id=game_id).delete()
    return redirect("community")