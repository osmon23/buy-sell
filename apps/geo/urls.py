from rest_framework import routers

from .views import GeoViewSet


router = routers.DefaultRouter()

router.register(r'', GeoViewSet, basename='geo')

urlpatterns = router.urls
