from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ('username','email','is_staff')
    fieldsets = UserAdmin.fieldsets + ((None,{'fields':("age","profile_photo",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields':("age","profile_photo",)}),)
