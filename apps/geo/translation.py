from modeltranslation.translator import register, TranslationOptions

from .models import Geo


@register(Geo)
class GeoTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )
