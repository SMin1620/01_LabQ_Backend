from django.urls import path
from .views import RainfallDrainAPI

app_name = 'api'

urlpatterns = [
    path('rainfall-drain/', RainfallDrainAPI.as_view(), name='rainfall-drain'),
    
]
