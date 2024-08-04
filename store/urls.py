from django.urls import path
from .views import HomeView, LibraryView, RegisterView, purchase_game

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('library/', LibraryView.as_view(), name='library'),
    path('Register/', RegisterView.as_view(), name='Register'),
    path('purchase/<int:game_id>/', purchase_game, name='purchase_game'),  # New URL pattern
]
