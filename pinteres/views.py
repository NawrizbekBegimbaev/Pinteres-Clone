from django.shortcuts import render
from pinteres.models import *
from pinteres.forms import CustomUserChangeForm,CustomUserCreationForm
from django.db.models import Q
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from pinteres.forms import PhotoForm

class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        if not self.success_url:
            raise ImproperlyConfigured("No URL to redirect to. Provide a success_url.")
        return str(self.success_url)  # success_url may be lazy

    def form_valid(self, form):
        form.save()
        return redirect('login1')

def category_list(request):
    category = Category.objects.all()
    context = {
        'category' : category
    }
    return render(request,'category.html',context)


def photo_list(request):
    photos = Photo.objects.all()
    context = {
        'photos' : photos
    }
    return render(request,'list.html',context)

def photo_index(request,pk):
    photo = Photo.objects.get(id=pk)
    photos = Photo.objects.filter(Q(category__name__icontains=photo.category))
    context = {
        'photo' : photo,
        'photos' : photos
    }
    return render(request,'index.html',context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/pinteres') # replace 'home' with your desired redirect url
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')




def search(request):
  query = request.GET.get('search')
  object_list = Photo.objects.filter(Q(title__icontains=query) | Q(category__name__icontains=query))
  context = {
    'object_list':object_list
  }
  return render(request, 'search.html', context)

def sign_out(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/pinteres')


def create(request):
  form = PhotoForm()
  category = Category.objects.all()
  users = CustomUser.objects.all()
  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('http://127.0.0.1:8000/pinteres')
  context = {
    'form':form,
    'category' : category,
    'users' : users

  }
  return render(request, 'create.html', context)