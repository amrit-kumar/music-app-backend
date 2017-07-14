from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from music_app.serializers import MusicTracksSerializers, GenreSerializers
from .models import MusicTracks,Genre


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100

class MusicTracksViewSet(viewsets.ModelViewSet):
    queryset = MusicTracks.objects.all()
    serializer_class = MusicTracksSerializers
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    pagination_class = StandardResultsSetPagination
    search_fields = ('title',)
    filter_fields = ('title',)

    @detail_route(methods=["GET"])
    def get_genre_by_id(self,request, pk=None):
        qsets=Genre.objects.filter(musictracks__id=pk)
        serialized=GenreSerializers(qsets,many=True)

        return Response(serialized.data)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
    # filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)