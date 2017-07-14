from django.conf.urls import  include, url
from rest_framework import routers
from music_app.views import MusicTracksViewSet,GenreViewSet


from django.contrib import admin
admin.autodiscover()


router=routers.DefaultRouter()
router.register(r'musictrack',MusicTracksViewSet)
router.register(r'genre',GenreViewSet)

urlpatterns = (
    # Examples:
    # url(r'^$', 'music.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)