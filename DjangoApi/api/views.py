from rest_framework.viewsets import ModelViewSet
from api.models import *
from api.serializers import *
# Create your views here.


class FlightListV(ModelViewSet):
    queryset = Passengers.objects.all()
    serializer_class = PassengersSerializer


class FlightListView(ModelViewSet):
    queryset = Flights.objects.all()
    serializer_class = FlightListSerializer

    def get_queryset(self):
        from_slug = self.request.query_params.get('from_field', None)
        to_slug = self.request.query_params.get('to', None)
        qs = None
        if from_slug and to_slug:
            from_field = Airports.objects.filter(iata = from_slug).first()
            to = Airports.objects.filter(iata = to_slug).first()
            qs = Flights.objects.filter(from_field = from_field, to = to )
            self.queryset = qs
        return self.queryset