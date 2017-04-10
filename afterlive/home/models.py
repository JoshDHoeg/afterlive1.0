from __future__ import unicode_literals

from django.db import models

class Link(models.Model):
    Facebook = models.CharField(max_length = 512, blank=True, null=True)
    Instagram = models.CharField(max_length = 512, blank=True, null=True)
    Youtube = models.CharField(max_length = 512, blank=True, null=True)
    Twitter = models.CharField(max_length = 512, blank=True, null=True)
    Tumblr = models.CharField(max_length = 512, blank=True, null=True)
    Soundcloud = models.CharField(max_length = 512, blank=True, null=True)
    Pinterest = models.CharField(max_length = 512, blank=True, null=True)
    Website = models.CharField(max_length = 512, blank=True, null=True)

    def __str__(self):
        return str(self.id);

class Photographer(models.Model):
    Name = models.CharField(max_length=140, blank=True, null=True)
    FirstName = models.CharField(max_length=140, blank=True, null=True)
    LastName = models.CharField(max_length=140, blank=True, null=True)
    Background = models.TextField(blank=True, null=True)
    Bio = models.TextField(blank=True, null=True)
    LinkID = models.ForeignKey(Link, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.FirstName) + " " + str(self.LastName)

class Venue(models.Model):
    Name = models.CharField(max_length=140, blank=True, null=True)
    City = models.CharField(max_length=140, blank=True, null=True)
    State = models.CharField(max_length=140, blank=True, null=True)
    Country = models.CharField(max_length=140, blank=True, null=True)
    LinkID = models.ForeignKey(Link, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.Name) + " " + str(self.City)

class Festival(models.Model):
    Name = models.CharField(max_length=140, primary_key=True)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Logo = models.TextField(blank=True, null=True)
    Background = models.TextField(blank=True, null=True)
    LinkID = models.ForeignKey(Link, on_delete=models.CASCADE, blank=True, null=True)
    VenueID = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.Name)


class Artist(models.Model):
    Name = models.CharField(max_length=140, primary_key=True)
    profile = models.TextField(blank=True, null=True)
    Background = models.TextField(blank=True, null=True)
    City = models.CharField(max_length=140, blank=True, null=True)
    Country = models.CharField(max_length=140, blank=True, null=True)
    Genre = models.CharField(max_length=140, blank=True, null=True)
    LinkID = models.ForeignKey(Link, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.Name)



class Festival_Artist(models.Model):
    ArtistID = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    FestivalID = models.ForeignKey(Festival, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.FestivalID) + " " + str(self.ArtistID)

class Festival_Photographer(models.Model):
    PhotographerID = models.ForeignKey(Photographer, on_delete=models.CASCADE, blank=True, null=True)
    FestivalID = models.ForeignKey(Festival, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.FestivalID) + " " + str(self.PhotographerID)

class Content(models.Model):
    Account = models.CharField(max_length=140, blank=True, null=True)
    ContentType = models.CharField(max_length=140, blank=True, null=True)
    Source = models.CharField(max_length=140, blank=True, null=True)
    ContentLink =  models.TextField(blank=True, null=True)
    FAID = models.ForeignKey(Festival_Artist, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.Account) + " | " + str(self.FAID)
