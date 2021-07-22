from django.urls import path
from django.urls.conf import include

from .views import index, contato


urlpatterns = [
    path('grappelli/', include ('grappelli.urls')), # grappelli URLS
    path('index', index),
    path('contato', contato),
]