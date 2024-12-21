from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Ticket
from .serializer import TicketSerializer, TicketCreateUpdateSerializer

class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TicketCreateUpdateSerializer
        return TicketSerializer
    
class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateUpdateSerializer

class TicketListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TicketCreateUpdateSerializer
        return TicketSerializer

class TicketListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TicketSerializer

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)  # assuming you have a user field in the Ticket model
