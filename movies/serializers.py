from rest_framework import serializers
from .models import Movie

class MoiveSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.first_name')
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'year', 'creator']
