from django.urls import path
from .views import heart_predict

urlpatterns = [
    path('', heart_predict, name='heart_predict'),
]