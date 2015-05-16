# -*- encoding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.utils.encoding import python_2_unicode_compatible
import time

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

    def as_json(self):
        return dict(
            name = self.name,
            name_rus = self.name_rus,
            title = self.title,
            title_rus = self.title_rus,
            time = self.time,
            year = self.year,
            imbdRating = self.imbdRating,
            estim_mid = self.estim_mid,
            estim_num = self.estim_num,
            pk = self.pk,
            poster_link = self.poster_link,
            country = [country.name for country in self.country.all()],
            directors = [director.name for director in self.directors.all()],
            actors = [actor.name for actor in self.actors.all()],
            genres = [genre.name for genre in self.genres.all()],
        )

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class MyUser(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    age = models.IntegerField(max_length=5, null=True, blank=True)
    sex = models.CharField(max_length=1,null=True,blank=True)
    friends = models.ManyToManyField("self",null=True,blank=True, symmetrical = False)
    likedComments = models.ManyToManyField("Comment",null=True,related_name="likedComments")
    dislikedComments = models.ManyToManyField("Comment",null=True,related_name="dislikedComments")
    # avatar = models.ImageField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Value(models.Model):
    values = models.IntegerField(max_length=2, null=False, blank=False)

    def __unicode__(self):
        return str(self.values.__str__())

    def __str__(self):
        return str(self.values.__str__())
#
#
class MyRating(models.Model):
    value = models.ForeignKey(Value, null=False, blank=False, related_name="value_rating")
    user = models.ForeignKey(MyUser, null=False, blank=False, related_name="user_rating_set")
    film = models.ForeignKey(Film,   null=False, blank=False, related_name="film_rating_set")
    timestamp = models.BigIntegerField(max_length=100, null=True, blank=True, default=10)

    def __unicode__(self):
        return "user = " + self.user + "; film = " + self.film + " ; value = " + str(self.value)

    def __str__(self):
        return "user = " + str(self.user) + "; film = " + str(self.film) + " ; value = " + str(self.value)

    def as_json(self):
        return dict(pk=self.pk, users = self.user.name,
                    film = self.film.name, film_id = self.film.pk, film_poster = self.film.poster_link,
                    film_num = self.film.estim_num, film_mid= self.film.estim_mid,
                    value = str(self.value),
                    timestamp = self.timestamp.__str__())

class Comment(models.Model):
    user = models.ForeignKey(MyUser,null=False, blank=False)
    film = models.ForeignKey(Film,null=False, blank=False)
    comment = models.TextField(max_length=255,null=False,blank=False)
    like = models.IntegerField(max_length=10,null=False,blank=False,default=0)
    dislike = models.IntegerField(max_length=10,null=False,blank=False,default=0)
    timestamp = models.BigIntegerField(max_length=100, null=False, blank=True, default=10)

    def __unicode__(self):
        return self.comment

    def __str__(self):
        return self.comment

    def as_json(self):
        return dict(pk=self.pk, users = self.user.name, comment = self.comment,
                    film = self.film.name, film_id = self.film.pk, film_poster = self.film.poster_link,
                    film_rus = self.film.name_rus,
                    cd = self.dislike,cl=self.like,
                    timestamp = self.timestamp.__str__())