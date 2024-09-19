from django.urls import path
from .views import *
urlpatterns = [

    path('dashboard',Dashboard),
    path('home', Home.as_view()),
    path('logout', logout_view),
]