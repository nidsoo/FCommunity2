
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [

path("", views.home, name="home" ),
path("community/" ,views.community,name="community"),
path("delete/<int:game_id>/", views.delete_game, name="delete_game"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
