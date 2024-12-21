from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializer import UserSerializer, UserCreateUpdateSerializer

class UserListCreateView(generics.ListCreateAPIView):
    """
    Vue pour lister tous les utilisateurs et en créer de nouveaux.
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        """
        Retourne le serializer approprié en fonction de la méthode HTTP.
        - POST : Utilise `UserCreateUpdateSerializer` pour la création.
        - GET : Utilise `UserSerializer` pour la lecture.
        """
        if self.request.method == 'POST':
            return UserCreateUpdateSerializer
        return UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vue pour récupérer, mettre à jour ou supprimer un utilisateur spécifique.
    """
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer
