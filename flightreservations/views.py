from django.shortcuts import render
from .serializers import flightserializer,reservationserializer
# Create your views here.
from . models import flight,reservation
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS,IsAuthenticatedOrReadOnly
from rest_framework import generics

class FlightUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
class FlightDetail(generics.ListCreateAPIView,FlightUserWritePermission):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = flight.objects.all()
    serializer_class = flightserializer

class ReservationDetail(generics.ListCreateAPIView,FlightUserWritePermission):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = reservation.objects.all()
    serializer_class = reservationserializer

