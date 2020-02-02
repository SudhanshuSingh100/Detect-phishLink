from django.urls import path

from static_serve.views import index

urlpatterns = [
    path('site', index),
]
