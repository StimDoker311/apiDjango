from rest_framework import serializers
from api.models import *


class PassengersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = ('id', 'first_name', 'last_name')

class AirportsSer(serializers.ModelSerializer):
    class Meta:
        model = Airports
        fields = ('name','iata')

class FlightListSerializer(serializers.ModelSerializer):
    from_field = AirportsSer(read_only=True)
    to = AirportsSer(read_only=True)

    class Meta:
        model = Flights
        fields = ('id','flight_code','from_field','to','cost')