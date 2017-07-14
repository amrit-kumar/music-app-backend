from rest_framework import serializers
from .models import MusicTracks,Genre


class MusicTracksSerializers(serializers.ModelSerializer):
    class Meta:
        model=MusicTracks
        fields = '__all__'

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields = '__all__'

