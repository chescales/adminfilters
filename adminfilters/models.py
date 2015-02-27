from __future__ import absolute_import, unicode_literals

from django.db import models


class Specie(models.Model):
    name = models.CharField(
        max_length=255,
    )
    binomial_name = models.CharField(
        max_length=255,
    )

    def __unicode__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(
        max_length=255,
    )
    specie = models.ForeignKey(
        to=Specie,
    )

    def __unicode__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(
        max_length=255,
    )
    breed = models.ForeignKey(
        to=Breed,
    )
    birth = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return "{} ({})".format(self.name, self.breed.name)