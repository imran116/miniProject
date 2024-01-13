from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-artist/', views.artist, name='add-artist'),
    path('edit-artist/<int:id>', views.editArtist, name='edit-artist'),
    path('delete-artist/<int:id>', views.deleteArtist, name='delete-artist'),
    path('artist-details/<int:id>', views.artistDetails, name='artist-details'),

]
