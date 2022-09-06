from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Profile

# Register your models here.


@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','is_staff']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('age',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields':('age',)}),)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','photo']
    raw_id_fields = ['user']
    