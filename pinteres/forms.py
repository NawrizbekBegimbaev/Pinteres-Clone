from django.forms import ModelForm
from pinteres.models import Photo,CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username','name','first_name', 'last_name', 'email', 'password1', 'password2']


