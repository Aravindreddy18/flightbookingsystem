from rest_framework import serializers
from . models import flight,reservation



class flightserializer(serializers.ModelSerializer):

    class Meta:
        model = flight
        fields = '__all__'

class reservationserializer(serializers.ModelSerializer):

    class Meta:
        model = reservation
        fields = '__all__'