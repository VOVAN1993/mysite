# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.utils.encoding import python_2_unicode_compatible

class Genre(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    name_rus = models.CharField(max_length=300, null=False, blank=False, default="N/A")

    def natural_key(self):
        return self.name

    def __unicode__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    name_rus = models.CharField(max_length=30, null=True, blank=False)

    def natural_key(self):
        return self.name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    name_rus = models.CharField(max_length=30, null=True, blank=False)

    def natural_key(self):
        return self.name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    name_rus = models.CharField(max_length=30, null=True, blank=False)

    def natural_key(self):
        return self.name

    def __unicode__(self):
        return self.name

class Film(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    name_rus = models.CharField(max_length=500, null=True, blank=False)
    title = models.CharField(max_length=8000, null=True, blank=False)
    title_rus = models.CharField(max_length=6000, null=True, blank=False)
    country = models.ManyToManyField(Country)
    time = models.CharField(max_length=15, null=True, blank=False)
    year = models.CharField(max_length=15, null=True, blank=False)
    imbdRating = models.FloatField(max_length=15, null=True, blank=False, default=0)
    imbdID = models.CharField(max_length=15, null=False, blank=False, default=0)
    estim_mid = models.FloatField(max_length=15,null=True,blank=False, default=0.0)
    estim_num = models.IntegerField(max_length=19,null=True,blank=False, default=0)
    poster_link = models.URLField(null=True)
    directors = models.ManyToManyField(Director, null=True)
    actors = models.ManyToManyField(Actor,null=True)
    genres = models.ManyToManyField(Genre,null=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name