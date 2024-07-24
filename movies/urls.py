from django.urls import path
from .import views

urlpatterns = [
    path('', views.ListCreateMovieAPIView.as_view(), name='get-movies'),
    path('movie/<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='update-delete-movies')
]
