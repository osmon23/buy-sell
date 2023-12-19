from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from .models import Geo


@admin.register(Geo)
class GeoAdmin(LeafletGeoAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'name',
    )
