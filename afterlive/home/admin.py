from django.contrib import admin
from home.models import *



class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'account_link')
    search_fields = ('username', 'email')
    list_display_links = ('username', 'account_link')
    class Meta:
        model = Account

admin.site.register(Account, AccountAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist_genre', 'artist_account')
    search_fields = ('name', 'artist_id')
    list_display_links = ('name', 'artist_account')
    class Meta:
        model = Artist

admin.site.register(Artist, ArtistAdmin)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('account', 'content_artist', 'content_festival', 'content_culture', 'content_type')
    search_fields = ('account', 'account')
    class Meta:
        model = Content


admin.site.register(Content, ContentAdmin)
admin.site.register(Culture)
admin.site.register(Family)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'festival_account', 'festival_venue')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'festival_id')
    list_display_links = ('name', 'festival_venue', 'festival_account')
    class Meta:
        model = Festival


admin.site.register(Festival, FestivalAdmin)
admin.site.register(Festival_Artist)
admin.site.register(Festival_Follower)
admin.site.register(Festival_Photographer)
admin.site.register(Genre)
admin.site.register(Identity)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('linkid', 'website', 'facebook', 'instagram', 'spotify', 'soundcloud')
    search_fields = ('linkid', 'website')
    list_display_links = ('website', 'facebook', 'instagram', 'spotify', 'soundcloud')
    class Meta:
        model = Link

admin.site.register(Link, LinkAdmin)

class PhotographerAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name', 'last_name', 'photographer_account', 'photographer_family' ,'photographer_identity')
    list_display_links = ('name', 'photographer_account', 'photographer_family' ,'photographer_identity')
    search_fields = ('name', 'first_name', 'last_name', 'photographer_id')
    class Meta:
        model = Photographer

admin.site.register(Photographer,PhotographerAdmin)
admin.site.register(Photographer_Artist)
admin.site.register(Photographer_Follower)
admin.site.register(Type)

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_family', 'user_account', 'user_country')
    search_fields = ('first_name', 'last_name', 'user_id')
    class Meta:
        model = User

admin.site.register(User, UserAdmin)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue_state', 'venue_country')
    search_fields = ('name', 'venue_id')
    class Meta:
        model = Venue

admin.site.register(Venue, VenueAdmin)
