from __future__ import absolute_import, unicode_literals

from django.db import models


class Species(models.Model):
    name = models.CharField(
        max_length=255,
    )
    binomial_name = models.CharField(
        max_length=255,
    )

    class Meta:
        verbose_name_plural = 'Species'

    def __unicode__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(
        max_length=255,
    )
    species = models.ForeignKey(
        to=Species,
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

    def get_species(self):
        return self.breed.species
    get_species.short_description = 'Species'