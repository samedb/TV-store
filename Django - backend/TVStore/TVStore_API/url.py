from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('tv', TVViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('me/', UserDetailView.as_view()),
    path('ocena/', OcenaView.as_view()),
    path('ocena/<str:ean>', OcenaView.as_view()),
    path('porudzbina/', PorudzbineView.as_view())
]
