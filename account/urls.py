from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path('signup/', SignupView.as_view() , name="list-create-user-view"),
    path('signin/', SigninView.as_view() , name="sigin-view")
]