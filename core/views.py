from rest_framework.generics import (CreateAPIView, ListAPIView,)
from .models import Reservation
from .serializers import ReservationSerializer


class ListReservationsView(ListAPIView):
    """
        List Reservations view
        list of all Reservations
    """

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class CreateReservationView(CreateAPIView):
    """
        Create Reservations view
    """

    serializer_class = ReservationSerializer