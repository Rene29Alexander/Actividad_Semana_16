from django.urls import path
from .views import *

urlpatterns = [
    
    path('', menu),
    path('about/', about),
]