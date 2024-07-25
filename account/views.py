from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import status
from django.shortcuts import render

# Create your views here.
class SignupView(generics.ListCreateAPIView):
    permission_classes  = []
    serializer_class    = SignupSerializer
    queryset            = User.objects.all().order_by('-id')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class SigninView(generics.GenericAPIView):
    permission_classes      = []
    serializer_class        = SigninSerializer
    queryset                = User.objects.all().order_by('-id')

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, 'react/index.html')