from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from adminfilters.models import Species, Breed, Pet
from adminfilters.list_filters import BreedListFilter, SpeciesListFilter


@admin.register(Species)
class SpecieAdmin(admin.ModelAdmin):
    list_display = ('name', 'binomial_name', )


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', )
    list_filter = (SpeciesListFilter, )


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_species', 'breed', 'birth', )
    list_filter = ('breed__species', BreedListFilter)
