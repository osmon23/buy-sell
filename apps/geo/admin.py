from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import Geo


@admin.register(Geo)
class GeoAdmin(TranslationAdmin, LeafletGeoAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'name',
    )
