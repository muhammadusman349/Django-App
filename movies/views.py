from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import MoiveSerializer
from .pagination import CustomPagination
from .filters import MovieFilter

# Create your views here.

class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MoiveSerializer 
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = [CustomPagination]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MoiveSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]