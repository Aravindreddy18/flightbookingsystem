from rest_framework import serializers
from . models import flight



class flightserializer(serializers.ModelSerializer):

    class Meta:
        model = flight
        fields = '__all__'