from django.urls import path
from .views import Register,addUSer

urlpatterns = [
    path('', Register, name='register'),
     path('addUSer/', addUSer, name='addUSer'),
    
]
