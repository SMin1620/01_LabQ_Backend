from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('test/<int:gubn>', views.test, name='test'),
    
]
