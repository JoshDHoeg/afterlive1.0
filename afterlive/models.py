# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(db_column='Username', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=256, blank=True, null=True)  # Field name made lowercase.
    background = models.TextField(db_column='Background', blank=True, null=True)  # Field name made lowercase.
    profile = models.TextField(db_column='Profile', blank=True, null=True)  # Field name made lowercase.
    bio = models.TextField(db_column='Bio', blank=True, null=True)  # Field name made lowercase.
    account_link = models.ForeignKey('Link', models.DO_NOTHING, db_column='Account_Link_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account'


class Artist(models.Model):
    artist_id = models.AutoField(db_column='Artist_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=256, blank=True, null=True)  # Field name made lowercase.
    artist_genre = models.ForeignKey('Genre', models.DO_NOTHING, db_column='Artist_Genre_ID', blank=True, null=True)  # Field name made lowercase.
    artist_identity = models.ForeignKey('Identity', models.DO_NOTHING, db_column='Artist_Identity_ID', blank=True, null=True)  # Field name made lowercase.
    artist_account = models.ForeignKey(Account, models.DO_NOTHING, db_column='Artist_Account_ID', blank=True, null=True)  # Field name made lowercase.
    artist_country = models.ForeignKey('Country', models.DO_NOTHING, db_column='Artist_Country_ID', blank=True, null=True)  # Field name made lowercase.
    artist_family = models.ForeignKey('Family', models.DO_NOTHING, db_column='Artist_Family_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'artist'


class ArtistFollower(models.Model):
    u = models.ForeignKey('User', models.DO_NOTHING, db_column='U_ID')  # Field name made lowercase.
    a = models.ForeignKey(Artist, models.DO_NOTHING, db_column='A_ID')  # Field name made lowercase.
    artist_user_id = models.AutoField(db_column='Artist_User_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'artist_follower'


class Content(models.Model):
    content_id = models.AutoField(db_column='Content_ID', primary_key=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=256)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=9)  # Field name made lowercase.
    content_value = models.TextField(db_column='Content_Value')  # Field name made lowercase.
    content_photographer = models.ForeignKey('Photographer', models.DO_NOTHING, db_column='Content_Photographer_ID', blank=True, null=True)  # Field name made lowercase.
    content_user = models.ForeignKey('User', models.DO_NOTHING, db_column='Content_User_ID', blank=True, null=True)  # Field name made lowercase.
    content_artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='Content_Artist_ID', blank=True, null=True)  # Field name made lowercase.
    content_festival = models.ForeignKey('Festival', models.DO_NOTHING, db_column='Content_Festival_ID', blank=True, null=True)  # Field name made lowercase.
    content_culture = models.ForeignKey('Culture', models.DO_NOTHING, db_column='Content_Culture_ID', blank=True, null=True)  # Field name made lowercase.
    content_type = models.ForeignKey('Type', models.DO_NOTHING, db_column='Content_Type_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'content'


class Country(models.Model):
    country_id = models.AutoField(db_column='Country_ID', primary_key=True)  # Field name made lowercase.
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(db_column='Country_Name', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class Culture(models.Model):
    culture_id = models.AutoField(db_column='Culture_ID', primary_key=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'culture'


class Family(models.Model):
    family_id = models.AutoField(db_column='Family_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'family'


class Festival(models.Model):
    festival_id = models.AutoField(db_column='Festival_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    festival_account = models.ForeignKey(Account, models.DO_NOTHING, db_column='Festival_Account_id', blank=True, null=True)  # Field name made lowercase.
    festival_venue = models.ForeignKey('Venue', models.DO_NOTHING, db_column='Festival_Venue_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'festival'


class FestivalArtist(models.Model):
    fl = models.ForeignKey(Festival, models.DO_NOTHING, db_column='Fl_ID')  # Field name made lowercase.
    a = models.ForeignKey(Artist, models.DO_NOTHING, db_column='A_ID')  # Field name made lowercase.
    festival_artist_id = models.AutoField(db_column='Festival_Artist_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'festival_artist'


class FestivalFollower(models.Model):
    festival_user_id = models.AutoField(db_column='Festival_User_ID', primary_key=True)  # Field name made lowercase.
    f = models.ForeignKey(Festival, models.DO_NOTHING, db_column='F_ID')  # Field name made lowercase.
    u = models.ForeignKey('User', models.DO_NOTHING, db_column='U_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'festival_follower'


class FestivalHasPhotographer(models.Model):
    festival_festival = models.ForeignKey(Festival, models.DO_NOTHING, db_column='Festival_Festival_ID')  # Field name made lowercase.
    photographer_photographer = models.ForeignKey('Photographer', models.DO_NOTHING, db_column='Photographer_Photographer_ID')  # Field name made lowercase.
    photographer_festival_id = models.IntegerField(db_column='Photographer_Festival_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'festival_has_photographer'


class Genre(models.Model):
    genre_id = models.AutoField(db_column='Genre_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genre'


class Identity(models.Model):
    identity_id = models.AutoField(db_column='Identity_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'identity'


class Likes(models.Model):
    content_content = models.ForeignKey(Content, models.DO_NOTHING, db_column='Content_Content_ID')  # Field name made lowercase.
    user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'likes'
        unique_together = (('content_content', 'user_user'),)


class Link(models.Model):
    linkid = models.AutoField(db_column='LinkID', primary_key=True)  # Field name made lowercase.
    facebook = models.CharField(db_column='Facebook', max_length=256, blank=True, null=True)  # Field name made lowercase.
    instagram = models.CharField(db_column='Instagram', max_length=256, blank=True, null=True)  # Field name made lowercase.
    youtube = models.CharField(db_column='Youtube', max_length=256, blank=True, null=True)  # Field name made lowercase.
    twitter = models.CharField(db_column='Twitter', max_length=256, blank=True, null=True)  # Field name made lowercase.
    spotify = models.CharField(db_column='Spotify', max_length=256, blank=True, null=True)  # Field name made lowercase.
    soundcloud = models.CharField(db_column='Soundcloud', max_length=256, blank=True, null=True)  # Field name made lowercase.
    tumblr = models.CharField(db_column='Tumblr', max_length=256, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=256, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'link'


class Photographer(models.Model):
    photographer_id = models.AutoField(db_column='Photographer_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True)  # Field name made lowercase.
    photographer_family = models.ForeignKey(Family, models.DO_NOTHING, db_column='Photographer_Family_ID', blank=True, null=True)  # Field name made lowercase.
    photographer_identity = models.ForeignKey(Identity, models.DO_NOTHING, db_column='Photographer_Identity_ID', blank=True, null=True)  # Field name made lowercase.
    photographer_account = models.ForeignKey(Account, models.DO_NOTHING, db_column='Photographer_Account_ID', blank=True, null=True)  # Field name made lowercase.
    photographer_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Photographer_Country_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'photographer'


class PhotographerArtist(models.Model):
    p = models.ForeignKey(Photographer, models.DO_NOTHING, db_column='P_ID')  # Field name made lowercase.
    a = models.ForeignKey(Artist, models.DO_NOTHING, db_column='A_ID')  # Field name made lowercase.
    photographer_artist_id = models.AutoField(db_column='Photographer_Artist_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'photographer_artist'


class PhotographerFollower(models.Model):
    u = models.ForeignKey('User', models.DO_NOTHING, db_column='U_ID')  # Field name made lowercase.
    p = models.ForeignKey(Photographer, models.DO_NOTHING, db_column='P_ID')  # Field name made lowercase.
    up_id = models.AutoField(db_column='UP_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'photographer_follower'


class PlaylistContent(models.Model):
    playlist_p = models.ForeignKey('UserPlaylists', models.DO_NOTHING, db_column='Playlist_p_ID')  # Field name made lowercase.
    playlist_c = models.ForeignKey(Content, models.DO_NOTHING, db_column='Playlist_c_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playlist_content'
        unique_together = (('playlist_p', 'playlist_c'),)


class State(models.Model):
    state_id = models.AutoField(db_column='State_ID', primary_key=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=256)  # Field name made lowercase.
    state_code = models.CharField(db_column='State_code', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'state'


class Type(models.Model):
    type_id = models.AutoField(db_column='Type_ID', primary_key=True)  # Field name made lowercase.
    content_type = models.CharField(db_column='Content_Type', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type'


class User(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True)  # Field name made lowercase.
    user_family = models.ForeignKey(Family, models.DO_NOTHING, db_column='User_Family_ID', blank=True, null=True)  # Field name made lowercase.
    user_identity = models.ForeignKey(Identity, models.DO_NOTHING, db_column='User_Identity_ID', blank=True, null=True)  # Field name made lowercase.
    user_account = models.ForeignKey(Account, models.DO_NOTHING, db_column='User_Account_ID', blank=True, null=True)  # Field name made lowercase.
    user_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='User_Country_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class UserPlaylistsHasUser(models.Model):
    user_playlists_playlistsid = models.ForeignKey('UserPlaylists', models.DO_NOTHING, db_column='User Playlists_PlaylistsID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_User_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user playlists_has_user'
        unique_together = (('user_playlists_playlistsid', 'user_user'),)


class UserPlaylists(models.Model):
    playlistid = models.AutoField(db_column='PlaylistID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256)  # Field name made lowercase.
    playlist_user = models.ForeignKey(User, models.DO_NOTHING, db_column='Playlist_User_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_playlists'


class Venue(models.Model):
    venue_id = models.AutoField(db_column='Venue_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=256, blank=True, null=True)  # Field name made lowercase.
    venue_state = models.ForeignKey(State, models.DO_NOTHING, db_column='Venue_State_ID', blank=True, null=True)  # Field name made lowercase.
    venue_country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Venue_Country_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venue'
