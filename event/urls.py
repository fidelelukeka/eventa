from django.urls import path
from .views import EventListCreateView, EventDetailView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='category-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='category-detail'),
]
