from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q

from . import team_maker

def index(request):
	context = {
		# # All baseball leagues
		# "leagues": League.objects.filter(sport = 'Baseball'),
		# # All womens' leagues
		# "leagues": League.objects.filter(name__contains = 'womens'),
		# # All leagues where sport is any type of hockey
		# "leagues": League.objects.filter(sport__contains = 'hockey'),
		# # All leagues where sport is something OTHER THAN football
		# "leagues": League.objects.exclude(sport = 'football'),
		# # All leagues that call themselves "conferences"
		# "leagues": League.objects.filter(name__contains = 'conference'),
		# # All leagues in the Atlantic region
		# "leagues": League.objects.filter(name__contains = 'Atlantic'),
		# "leagues": League.objects.all(),

		# # All teams based in Dallas
		# "teams": Team.objects.filter(location = 'Dallas'),
		# # All teams named the Raptors
		# "teams": Team.objects.filter(team_name__contains = 'Raptors'),
		# # All teams whose location includes "City"
		# "teams": Team.objects.filter(location__contains = 'City'),
		# # All teams whose names begin with "T"
		# "teams": Team.objects.filter(location__istartswith = 'T'),
		# # All teams, ordered alphabetically by location
		# "teams": Team.objects.order_by('location').all(),
		# # All teams, ordered by team name in reverse alphabetical order
		# "teams": Team.objects.order_by('-team_name').all(),
		# "teams": Team.objects.all(),
		
		# # Every player with last name "Cooper"
		# "players": Player.objects.filter(last_name = 'Cooper'),
		# # Every player with first name "Joshua"
		# "players": Player.objects.filter(first_name = 'Joshua'),
		# # Every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
		# "players": Player.objects.filter(last_name = 'Cooper').exclude(first_name = 'Joshua'),
		# All players with first name "Alexander" OR first name "Wyatt"
		"players": Player.objects.filter(Q(first_name = 'Alexander') | Q(first_name='Wyatt')),
		# "players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")