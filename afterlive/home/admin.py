from django.contrib import admin
from home.models import *

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'city')
    list_filter = ('name', 'city')
    search_fields = ('name', 'city')
    class Meta:
        model = Artist

admin.site.register(Artist, ArtistAdmin)

admin.site.register(Artist_Follower)

admin.site.register(Content)

admin.site.register(Culture)

admin.site.register(Culture_Festival)

admin.site.register(Family)

class FestivalView(admin.ModelAdmin):
    list_display = ('__str__','name', 'start_date', 'end_date', 'festival_venue')
    list_filter = ('name', 'start_date', 'end_date')
    search_fields = ('name', 'start_date', 'end_date')
    class Meta:
        model = Festival

admin.site.register(Festival, FestivalView)

admin.site.register(Festival_Follower)

admin.site.register(Festival_Artist)

admin.site.register(Festival_Photographer)

admin.site.register(Identity)

admin.site.register(Likes)

admin.site.register(Link)

admin.site.register(Photographer)

admin.site.register(Photographer_Follower)

admin.site.register(Photographer_Artist)

admin.site.register(Playlist_Content)

class UserView(admin.ModelAdmin):
    list_display = ('__str__', 'username', 'email', 'first_name', 'last_name')
    list_filter = ('username', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name')
    class Meta:
        model = User

admin.site.register(User, UserView)

admin.site.register(UserPlaylists)

admin.site.register(Venue)
