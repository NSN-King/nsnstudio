from django.urls import path

from studio.views import index


urlpatterns = [
    path('', index),
]
