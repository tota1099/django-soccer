from django.contrib import admin
from soccer.models import Position, Player, Games, GamesCards, GamesGoals
from django.conf.locale.en import formats as en_formats


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'birth_date')
    search_fields = ['first_name', 'position__name']
    list_filter = ['first_name', 'last_name', 'position', 'birth_date']

admin.site.register(Player, PlayerAdmin)
admin.site.register(Position)
admin.site.register(Games)
admin.site.register(GamesGoals)
admin.site.register(GamesCards)