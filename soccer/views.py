from django.shortcuts import render
from django.http import HttpResponse
from soccer.models import Player, Games, GamesCards, GamesGoals
from django.db.models import Count

def players(request):
    players = Player.objects.all()

    context = {
        "players": players
    }

    return render(request, 'soccer/playersList.html', context)


def games(request):
    games = Games.objects.all().annotate(Count('gamesgoals'))

    context = {
        "games": games
    }
    return render(request, 'soccer/gamesList.html', context)

def gameDetail(request, game_id):
    game = Games.objects.get(id=game_id)
    cards = GamesCards.objects.filter(game=game)
    goals = GamesGoals.objects.filter(game=game)

    context = {
        "game": game,
        "cards": cards,
        "goals": goals
    }
    return render(request, 'soccer/gameDetail.html', context)