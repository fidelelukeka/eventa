from django.urls import path
from .views import TicketDetailView, TicketListCreateView

urlpatterns = [
    path('tickets/', TicketListCreateView.as_view(), name='event-list-create'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='event-detail'),
]
