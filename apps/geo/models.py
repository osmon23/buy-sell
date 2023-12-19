from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Geo(models.Model):
    point = models.PointField(
        _('Point'),
    )
    polygon = models.MultiPolygonField(
        _('Polygon')
    )
    name = models.CharField(
        _('Name'),
        max_length=255,
    )

    def __str__(self):
        return 'qwerty'

    class Meta:
        verbose_name = _('Geo')
        verbose_name_plural = _('Geos')
