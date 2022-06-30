from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('test/', views.Test.as_view(), name='test'),
    
]
