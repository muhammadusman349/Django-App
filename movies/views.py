from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Movie
from .permissions import IsOwnerOrReadOnly
from .serializers import MoiveSerializer
from .pagination import CustomPagination
from .filters import MovieFilter
from rest_framework.exceptions import PermissionDenied
# Create your views here.

class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MoiveSerializer 
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = [CustomPagination]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MovieFilter
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(creator=self.request.user)
        else:
            raise PermissionDenied("Authentication required to create a movie.")

class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MoiveSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]