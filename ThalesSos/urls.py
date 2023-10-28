from django.urls import path
from . import views

urlpatterns = [
    # Define the URL pattern for /transcribe
    path('transcribe', views.transcribe_google, name='transcribe_google'),
    # Add more URL patterns as needed
    path('administrador', views.administrador, name='administrador'),
    path('home', views.home, name='home'),
    path('delete_warning/<int:id>/', views.delete_warning, name='delete_warning'),
    path('delete_categorie/<int:id>/', views.delete_categorie, name='delete_categorie'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_warning/', views.add_warning, name='add_warning'),
    path('categories/update/', views.update_category, name='update_category'),
    path('update_warning/', views.update_warning, name='update_warning'),
]