from .serializers import ArtistSerializer, WorkSerializer
from Artist.models import Artist_t, Work
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class ArtSet(viewsets.ModelViewSet):
    queryset = Artist_t.objects.all()
    serializer_class = ArtistSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # filter_backends = [SearchFilter]
    filterset_fields = ['work']
    search_fields = ['name']

class WorkSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]