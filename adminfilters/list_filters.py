from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from adminfilters.models import Species, Breed


class BreedListFilter(admin.SimpleListFilter):
    """
    This filter is an example of how to combine two different Filters to work together.
    """
    # Human-readable title which will be displayed in the right admin sidebar just above the filter
    # options.
    title = 'breed'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'breed'

    # Custom attributes
    related_filter_parameter = 'breed__species__id__exact'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        queryset = Breed.objects.order_by('species_id')
        if self.related_filter_parameter in request.GET:
            queryset = queryset.filter(species_id=request.GET[self.related_filter_parameter])
        list_of_questions = [(str(breed.id), breed.name) for breed in queryset]
        return sorted(list_of_questions, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            return queryset.filter(breed_id=self.value())
        return queryset


class SpeciesListFilter(admin.SimpleListFilter):
    """
    This filter will always return a subset of the instances in a Model, either filtering by the
    user choice or by a default value.
    """
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'species'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'species'

    default_value = None

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        queryset = Species.objects.all()
        list_of_species = [(str(species.id), species.name) for species in queryset]
        return sorted(list_of_species, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value to decide how to filter the queryset.
        if self.value():
            return queryset.filter(species_id=self.value())
        return queryset

    def value(self):
        """
        Overriding this method will allow us to always have a default value.
        """
        value = super(SpeciesListFilter, self).value()
        if value is None:
            if self.default_value is None:
                # If there is at least one Species, return the first by name. Otherwise, None.
                first_species = Species.objects.order_by('name').first()
                value = None if first_species is None else first_species.id
                self.default_value = value
            else:
                value = self.default_value
        return str(value)
