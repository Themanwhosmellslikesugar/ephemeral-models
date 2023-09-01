"""The module contains views of weather app models in the admin panel."""

from django.conf import settings
from django.contrib import admin

from weather.change_lists import ForecastDayChangeList
from weather.models import ForecastDay


class EphemeralAdmin(admin.ModelAdmin):
    """The base class for the admin panel for ephemeral models."""

    change_list_class = ForecastDayChangeList

    def get_queryset(self, request):
        """Overrides the returned list of objects."""

        return self.model.objects.none()

    def get_changelist(self, _request, **_kwargs):
        """Returns the overridden `ChangeList` class to use on the object list page."""

        return self.change_list_class


@admin.register(ForecastDay)
class AccountWithStoriesAdmin(EphemeralAdmin):
    """View of the ForecastDay model in the admin panel."""

    list_display = ('created_at', 'max_temp', 'avg_temp', 'max_wind', 'avg_humidity', 'condition')

    def changelist_view(self, request, extra_context=None):
        """Allows you to throw additional information when displaying data as a list
        in admin panel.
        """

        extra_context = extra_context or {}
        extra_context.update({
            'title': (
                f'Weather forecast for {settings.WEATHER_API_DAYS} days in '
                f'{settings.WEATHER_API_CITY.capitalize()}'
            )
        })

        return super().changelist_view(request, extra_context=extra_context)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
