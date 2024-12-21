from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer pour la lecture des utilisateurs.
    Inclut tous les champs nécessaires pour afficher les détails d'un utilisateur.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'userlastname', 'adresse', 'email', 'telephone']

class UserCreateUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'userlastname', 'adresse', 'password', 'email', 'telephone']

    def create(self, validated_data):
        # Hache le mot de passe avant de créer l'utilisateur
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Hache le mot de passe lors de la mise à jour, si fourni
        password = validated_data.pop('password', None)
        if password:
            instance.password = make_password(password)
        return super().update(instance, validated_data)
