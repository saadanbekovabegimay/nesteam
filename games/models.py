from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
class Game(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    genre = models.ForeignKey(
        to=Genre,
        on_delete=models.PROTECT,
        null=True,
    )
    studio = models.ForeignKey(
        to='Studio',
        on_delete=models.PROTECT,
        null=True,
    )
    def __str__(self):
        return self.name

class Studio(models.Model):
    name = models.CharField(max_length=100)
    workers_count = models.PositiveIntegerField()
    games_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


