from django_filters import rest_framework as filters
from .models import Movie

class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    genre = filters.CharFilter(lookup_expr='icontains')
    year = filters.NumberFilter()
    year__gt = filters.NumberFilter(field_name='year' ,lookup_expr='gt')
    year__lt = filters.NumberFilter(field_name='year' ,lookup_expr='lt')
    creator = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Movie
        fields = ['title', 'genre', 'year', 'year__gt', 'year__lt', 'creator__first_name']
    