from django.contrib import admin
from .models import MusicTracks,Genre

# Register your models here.
admin.site.register(Genre)
admin.site.register(MusicTracks)