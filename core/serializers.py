from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):

    """
        Reservation CRUD Serializer
    """

    class Meta:
        model = Reservation
        fields = ['pk', 'description']