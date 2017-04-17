# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Artist(models.Model):
    artist_id = models.AutoField(db_column='Artist_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    profile = models.FileField(upload_to='home/uploads/profiles/', blank=True, null=True)  # Field name made lowercase.
    background = models.FileField(upload_to='home/uploads/backrgounds/', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    artist_link = models.ForeignKey('Link', models.DO_NOTHING, db_column='Artist_Link_ID', blank=True, null=True)  # Field name made lowercase.
    artist_identity = models.ForeignKey('Identity', models.DO_NOTHING, db_column='Artist_Identity_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'artist'

    def __str__(self):
        return self.name

class Artist_Follower(models.Model):
    u = models.ForeignKey('User', models.DO_NOTHING, db_column='U_ID', blank=True, null=True)  # Field name made lowercase.
    a = models.ForeignKey(Artist, models.DO_NOTHING, db_column='A_ID', blank=True, null=True)  # Field name made lowercase.
    au_id = models.AutoField(db_column='AU_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'artist follower'

    def __str__(self):
        return self.u.first_name + " follows " + self.a.name

class Content(models.Model):
    content_id = models.AutoField(db_column='Content_ID', primary_key=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=150)  # Field name made lowercase.
    ContentType = models.CharField(db_column='Type', max_length=55)  # Field name made lowercase.
    origin = models.CharField(db_column='Origin', max_length=55)  # Field name made lowercase.
    source = models.TextField(blank=True, null=True)
    content_photographer = models.ForeignKey('Photographer', models.DO_NOTHING, db_column='Content_Photographer_ID', blank=True, null=True)  # Field name made lowercase.
    content_user = models.ForeignKey('User', models.DO_NOTHING, db_column='Content_User_ID', blank=True, null=True)  # Field name made lowercase.
    content_artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='Content_Artist_ID', blank=True, null=True)  # Field name made lowercase.
    content_festival = models.ForeignKey('Festival', models.DO_NOTHING, db_column='Content_Festival_ID', blank=True, null=True)  # Field name made lowercase.
    content_culture = models.ForeignKey('Culture', models.DO_NOTHING, db_column='Content_Culture_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'content'


class Culture(models.Model):
    cultureid = models.AutoField(db_column='CultureID', primary_key=True)  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=155)  # Field name made lowercase.

    class Meta:
        db_table = 'culture'

    def __str__(self):
        return self.tag


class Culture_Festival(models.Model):
    culture_cultureid = models.ForeignKey(Culture, models.DO_NOTHING, db_column='Culture_CultureID', blank=True, null=True)  # Field name made lowercase.
    festival_festival = models.ForeignKey('Festival', models.DO_NOTHING, db_column='Festival_Festival_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'culture_has_festival'
        unique_together = (('culture_cultureid', 'festival_festival'),)


class Family(models.Model):
    familyid = models.AutoField(db_column='FamilyID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    festival_artist = models.ForeignKey(Artist, models.DO_NOTHING, db_column='Festival_Artist_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'family'

    def __str__(self):
        return self.name


class Festival(models.Model):
    festival_id = models.AutoField(db_column='Festival_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=155)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_date = models.DateField(db_column='End Date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profile = models.FileField(upload_to='home/uploads/profiles/', blank=True, null=True)  # Field name made lowercase.
    background = models.FileField(upload_to='home/uploads/backrgounds/', blank=True, null=True)  # Field name made lowercase.
    bio = models.TextField(db_column='Bio')  # Field name made lowercase.
    festival_link = models.ForeignKey('Link', models.DO_NOTHING, db_column='Festival_Link_ID', blank=True, null=True)  # Field name made lowercase.
    festival_venue = models.ForeignKey('Venue', models.DO_NOTHING, db_column='festival_venue_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'festival'

    def __str__(self):
        return str(self.festival_id)


class Festival_Follower(models.Model):
    fu_id = models.AutoField(db_column='FU_ID', primary_key=True)  # Field name made lowercase.
    f = models.ForeignKey(Festival, models.DO_NOTHING, db_column='F_ID', blank=True, null=True)  # Field name made lowercase.
    u = models.ForeignKey('User', models.DO_NOTHING, db_column='U_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'festival follower'


class Festival_Artist(models.Model):
    fl = models.ForeignKey(Festival, models.DO_NOTHING, db_column='Fl_ID', blank=True, null=True)  # Field name made lowercase.
    a = models.ForeignKey(Artist, models.DO_NOTHING, db_column='A_ID', blank=True, null=True)  # Field name made lowercase.
    fa_id = models.AutoField(db_column='FA_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'festival_artist'


class Festival_Photographer(models.Model):
    festival_festival = models.ForeignKey(Festival, models.DO_NOTHING, db_column='Festival_Festival_ID', blank=True, null=True)  # Field name made lowercase.
    photographer_photographer = models.ForeignKey('Photographer', models.DO_NOTHING, db_column='Photographer_Photographer_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'festival_photographer'
        unique_together = (('festival_festival', 'photographer_photographer'),)


class Identity(models.Model):
    identityid = models.AutoField(db_column='IdentityID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'identity'

    def __str__(self):
        return self.name


class Likes(models.Model):
    content_content = models.ForeignKey(Content, models.DO_NOTHING, db_column='Content_Content_ID', blank=True, null=True)  # Field name made lowercase.
    user_user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_User_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'likes'
        unique_together = (('content_content', 'user_user'),)


class Link(models.Model):
    linkid = models.AutoField(db_column='LinkID', primary_key=True)  # Field name made lowercase.
    facebook = models.CharField(db_column='Facebook', max_length=255, blank=True, null=True)  # Field name made lowercase.
    instagram = models.CharField(db_column='Instagram', max_length=255, blank=True, null=True)  # Field name made lowercase.
    youtube = models.CharField(db_column='Youtube', max_length=255, blank=True, null=True)  # Field name made lowercase.
    twitter = models.CharField(db_column='Twitter', max_length=255, blank=True, null=True)  # Field name made lowercase.
    spotify = models.CharField(db_column='Spotify', max_length=255, blank=True, null=True)  # Field name made lowercase.
    soundcloud = models.CharField(db_column='Soundcloud', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tumblr = models.CharField(db_column='Tumblr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'link'

    def __str__ (self):
        return str(self.facebook)


class Photographer(models.Model):
    photographer_id = models.AutoField(db_column='Photographer_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=150)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=150)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64)  # Field name made lowercase.
    first_name = models.CharField(db_column='First Name', max_length=64)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last Name', max_length=64)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bio = models.TextField(db_column='Bio', blank=True, null=True)  # Field name made lowercase.
    profile = models.FileField(upload_to='home/uploads/profiles/', blank=True, null=True)  # Field name made lowercase.
    background = models.FileField(upload_to='home/uploads/backrgounds/', blank=True, null=True)  # Field name made lowercase.
    Gender_Types = (
        ('m', 'male'),
        ('f', 'female'),
    )
    gender = models.CharField(db_column='Gender',max_length=1, choices=Gender_Types, blank=True, null=True)  # Field name made lowercase.
    photographer_link = models.ForeignKey(Link, models.DO_NOTHING, db_column='Photographer_Link_ID', blank=True, null=True)  # Field name made lowercase.
    photographer_family = models.ForeignKey(Family, models.DO_NOTHING, db_column='Photographer_Family_ID', blank=True, null=True)  # Field name made lowercase.
    photographer_identity = models.ForeignKey(Identity, models.DO_NOTHING, db_column='Photographer_Identity_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'photographer'

    def __str__(self):
        return self.name


class Photographer_Follower(models.Model):
    u = models.ForeignKey('User', models.DO_NOTHING, db_column='U_ID', blank=True, null=True)  # Field name made lowercase.
    p = models.ForeignKey(Photographer, models.DO_NOTHING, db_column='P_ID', blank=True, null=True)  # Field name made lowercase.
    up_id = models.AutoField(db_column='UP_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'photographer follower'


class Photographer_Artist(models.Model):
    p = models.ForeignKey(Photographer, models.DO_NOTHING, db_column='P_ID', blank=True, null=True)  # Field name made lowercase.
    a = models.ForeignKey(Artist, models.DO_NOTHING, db_column='A_ID', blank=True, null=True)  # Field name made lowercase.
    pa_id = models.AutoField(db_column='PA_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'photographer_artist'


class Playlist_Content(models.Model):
    playlist_p = models.ForeignKey('UserPlaylists', models.DO_NOTHING, db_column='Playlist_p_ID', blank=True, null=True)  # Field name made lowercase.
    playlist_c = models.ForeignKey(Content, models.DO_NOTHING, db_column='Playlist_c_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'playlist content'
        unique_together = (('playlist_p', 'playlist_c'),)


class User(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=64)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=64)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    first_name = models.CharField(db_column='First Name', max_length=64)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last Name', max_length=64)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gender = models.CharField(db_column='Gender', max_length=6)  # Field name made lowercase.
    bio = models.TextField(db_column='Bio')  # Field name made lowercase.
    profile = models.FileField(upload_to='home/uploads/profiles/', blank=True, null=True)  # Field name made lowercase.
    background = models.FileField(upload_to='home/uploads/backrgounds/', blank=True, null=True)  # Field name made lowercase.
    user_link = models.ForeignKey(Link, models.DO_NOTHING, db_column='User_Link_ID', blank=True, null=True)  # Field name made lowercase.
    user_family = models.ForeignKey(Family, models.DO_NOTHING, db_column='User_Family_ID', blank=True, null=True)  # Field name made lowercase.
    user_identity = models.ForeignKey(Identity, models.DO_NOTHING, db_column='User_Identity_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.user_id


class UserPlaylists(models.Model):
    playlistid = models.AutoField(db_column='PlaylistID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.
    playlist_user = models.ForeignKey(User, models.DO_NOTHING, db_column='Playlist_User_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'user playlists'


class UserPlaylists_User(models.Model):
    user_playlists_playlistsid = models.ForeignKey(UserPlaylists, models.DO_NOTHING, db_column='User Playlists_PlaylistsID', default=0, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_user = models.ForeignKey(User, models.DO_NOTHING, db_column='User_User_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'user playlists_has_user'
        unique_together = (('user_playlists_playlistsid', 'user_user'),)


class Venue(models.Model):
    venue_id = models.AutoField(db_column='Venue_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, default='null')  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=155)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=155)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=155)  # Field name made lowercase.
    venue_link = models.ForeignKey(Link, models.DO_NOTHING, db_column='Venue_Link_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'venue'
