from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from adminfilters.models import Specie, Breed, Pet
from adminfilters.list_filters import BreedListFilter


@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    list_display = ('name', 'binomial_name', )


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'specie', )


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_specie', 'breed', 'birth', )
    list_filter = ('breed__specie', BreedListFilter)
