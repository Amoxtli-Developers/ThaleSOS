from django.urls import path
from . import views

urlpatterns = [
    # Define the URL pattern for /transcribe
    path('transcribe', views.transcribe_google, name='transcribe_google'),
    # Add more URL patterns as needed
]