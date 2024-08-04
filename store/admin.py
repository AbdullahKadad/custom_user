from django.contrib import admin
from .models import CustomUser, Game, Library
from django.contrib.auth.admin import UserAdmin
from .forms import ChangeForm, CreationForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CreationForm
    form = ChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'balance']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Game)
admin.site.register(Library)