from django.contrib import admin
from django.conf.urls import url
from soccer import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('soccer/players', views.players, name="soccer.listPlayers"),
    url('soccer/games', views.games, name="soccer.listGames"),
    url('soccer/gameDetail/(?P<game_id>\d+)', views.gameDetail, name="soccer.gameDetail"),
    url('', views.players, name="soccer.listPlayers")
]
