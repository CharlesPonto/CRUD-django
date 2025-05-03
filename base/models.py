from django.db import models

# Create your models here.


class Game(models.Model):
    game = models.CharField(max_length=20)
    description = models.TextField(null=True)

    def __str__(self):
        return self.game
    
class Player(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.username