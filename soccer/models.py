from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Games(models.Model):
    rival_team = models.CharField(max_length=100)
    date = models.DateField()
    goals_against = models.IntegerField()

    def __str__(self):
        return "vs " + self.rival_team

    class Meta:
        verbose_name_plural = "Games"

class GamesGoals(models.Model):
    note = models.CharField(max_length=255, blank=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    minute = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = "Games Goals"

    def __str__(self):
        return self.game.rival_team + ' - ' + self.player.first_name + ' ' + self.player.last_name + ' - Minute: ' + str(self.minute)

class GamesCards(models.Model):
    TYPE_CHOICES = (
        ('yellow','yellow'),
        ('red','red')
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=6)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    minute = models.IntegerField(max_length=3, default=0)


    class Meta:
        verbose_name_plural = "Games Cards"

    def __str__(self):
        return self.game.rival_team + ' - ' + self.player.first_name + ' ' + self.player.last_name + ' - Minute: ' + str(
            self.minute)