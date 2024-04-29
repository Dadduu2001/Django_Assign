from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtSet, WorkSet

rout = DefaultRouter()
rout.register('artist', ArtSet, basename='artist')
rout.register('work', WorkSet, basename='work')

urlpatterns = [
    path('', include(rout.urls)),  
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),  
]
