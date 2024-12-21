from rest_framework import serializers
from .models import Event
from category.serializer import CategorySerializer  # Import absolu pour CategorySerializer

class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Sérialiser l'objet Category (lecture seule)
    username = serializers.StringRelatedField()  # Afficher le nom de l'utilisateur au lieu de l'objet User

    class Meta:
        model = Event
        fields = ['id', 'category', 'titre', 'username', 'is_free', 'price', 'date', 'lieu']

class EventCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['category', 'titre', 'username', 'is_free', 'price', 'date', 'lieu']
        
    def get_category(self, instance):
        queryset = instance.category.filter(active = True)
        serializer = CategorySerializer(queryset, many= True)
        return serializer.data
