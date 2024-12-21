from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path('category/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]
