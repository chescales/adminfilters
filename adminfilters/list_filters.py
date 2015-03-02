from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from adminfilters.models import Specie, Breed, Pet


class BreedListFilter(admin.SimpleListFilter):
    """
    Human-readable title which will be displayed in the right admin sidebar just above the filter
    options.

    This filter is an example of how to combine two different Filters to work together.
    """
    title = 'breed'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'breed'

    # Custom attributes
    related_filter_parameter = 'breed__specie__id__exact'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list_of_questions = []
        queryset = Breed.objects.order_by('specie_id')
        if self.related_filter_parameter in request.GET:
            queryset = queryset.filter(specie_id=request.GET[self.related_filter_parameter])
        for breed in queryset:
            list_of_questions.append(
                (str(breed.id), breed.name)
            )
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


# class TopicListFilter(admin.SimpleListFilter):
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = _('topic')
#
#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'topic'
#
#     default_value = None
#
#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         list_of_topics = []
#         queryset = Topic.objects.exclude(deleted=True)
#         for t in queryset:
#             list_of_topics.append(
#                 (str(t.id), t.title)
#             )
#         return list_of_topics
#
#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value to decide how to filter the queryset.
#         if self.value():
#             request.path += '?topic={}'.format(self.value())
#             request.path_info += '?topic={}'.format(self.value())
#             return queryset.filter(topic_id=self.value())
#         return queryset
#
#     def value(self):
#         value = super(TopicListFilter, self).value()
#         if value is None:
#             if self.default_value is None:
#                 value = get_default_topic()
#                 self.default_value = value
#             else:
#                 value = self.default_value
#         return str(value)