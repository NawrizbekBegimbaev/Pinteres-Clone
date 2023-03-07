from django.contrib import admin
from pinteres.models import *
from pinteres.forms import *
from django.contrib.auth.admin import UserAdmin


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_display = ('nameuser',)

@admin.register(Category)
class CategortyAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_display = ('name',)

@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','name','is_staff',]
    list_display_links = ['username',]
    fieldsets = UserAdmin.fieldsets + ((None,{'fields' : ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields' : ("name",)}),)