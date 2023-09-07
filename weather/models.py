"""The module contains weather app models."""

from django.db import models


class BaseEphemeralModel(models.Model):
    """Base class for models that do not need to be stored in databases. Objects of
    such models receive data from other sources.
    """

    def _prepare_related_fields_for_save(self, operation_name, fields=None):
        """Don't save objects of other models."""

    class Meta:
        abstract = True


class ForecastDay(BaseEphemeralModel):
    """Describes the weather forecast for the day."""

    created_at = models.DateField('Date', blank=False, null=False)
    max_temp = models.DecimalField('Max temperature (°C)', max_digits=8, decimal_places=2)
    avg_temp = models.DecimalField('Avg temperature (°C)', max_digits=8, decimal_places=2)
    max_wind = models.DecimalField('Max wind (kph)', max_digits=8, decimal_places=2)
    avg_humidity = models.DecimalField('Avh humidity', max_digits=8, decimal_places=2)
    condition = models.CharField('Condition', max_length=128)

    class Meta:
        verbose_name = 'Daily weather forecast'
        verbose_name_plural = 'Weather forecast'
