from rest_framework import serializers
from .models import Ticket
from event.serializer import EventSerializer  # Import absolu pour CategorySerializer

class TicketSerializer(serializers.ModelSerializer):
    event = EventSerializer()  # Sérialiser l'objet Event (lecture seule)
    username = serializers.StringRelatedField()  # Afficher le nom de l'utilisateur au lieu de l'objet User

    class Meta:
        model = Ticket
        fields = ['id', 'event', 'owner']

class TicketCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['event', 'owner']
