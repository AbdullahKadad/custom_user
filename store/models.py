from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    balance = models.DecimalField(default=10000, max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.username

class Game(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img_url = models.URLField()

    def __str__(self):
        return self.name

class Library(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'game')  # Ensure a game can only appear once per user

    def __str__(self):
        return f"{self.user.username} - {self.game.name}"
