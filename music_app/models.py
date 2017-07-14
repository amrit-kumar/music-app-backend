from django.db import models

# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class MusicTracks(models.Model):
    title=models.CharField(max_length=50)
    genre=models.ManyToManyField(Genre,null=True,blank=True)
    rating=models.IntegerField()
    def __str__(self):
        return self.title


