from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Library
from django.views.generic.edit import CreateView
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
class HomeView(ListView):
    model = Game
    template_name = 'home.html'
    context_object_name = 'games'

class LibraryView(LoginRequiredMixin, ListView):
    model = Library
    template_name = 'library.html'
    context_object_name = 'libraries'

    def get_queryset(self):
        # Get the games for the logged-in user
        return Library.objects.filter(user=self.request.user)
    

class RegisterView(CreateView):
    form_class = CreationForm
    template_name = 'registration/Register.html'
    success_url = reverse_lazy('login')

@login_required
def purchase_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    user = request.user

    if user.balance < game.price:
        messages.error(request, "Insufficient balance to purchase this game.")
        return redirect('Home')

    # Check if the user already owns the game
    if Library.objects.filter(user=user, game=game).exists():
        messages.info(request, "You already own this game.")
        return redirect('Home')

    # Deduct the price from the user's balance
    user.balance -= game.price
    user.save()

    # Add the game to the user's library
    Library.objects.create(user=user, game=game)

    messages.success(request, "Purchase successful!")
    return redirect('Home')