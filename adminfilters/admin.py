from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from adminfilters.models import Specie, Breed, Pet


@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    list_display = ('name', 'binomial_name', )
