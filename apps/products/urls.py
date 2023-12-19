from django.urls import path

from .views import CategoryListAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
]
