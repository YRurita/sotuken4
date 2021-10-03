from django.db.models.query import QuerySet
from django.shortcuts import render

from rest_framework import viewsets

from .models import GridItem, person_in_the_room, num_of_people
from .serializers import GridItemSerializer, person_in_the_roomSerializer, num_of_peopleSerializer

class GridItemViewSet(viewsets.ModelViewSet):
    queryset = GridItem.objects.all()
    serializer_class = GridItemSerializer

class person_in_the_roomViewSet(viewsets.ModelViewSet):
    queryset = person_in_the_room.objects.all()
    serializer_class = person_in_the_roomSerializer

class num_of_peopleViewSet(viewsets.ModelViewSet):
    queryset = num_of_people.objects.all()
    serializer_class = num_of_peopleSerializer