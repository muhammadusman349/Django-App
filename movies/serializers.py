from rest_framework import serializers
from .models import Movie

class MoiveSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.first_name')
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'year', 'creator']

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)