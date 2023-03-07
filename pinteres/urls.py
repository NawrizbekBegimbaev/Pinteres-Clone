from django.urls import path
from pinteres.views import *

urlpatterns = [
    path('',photo_list),
    path('<int:pk>/',photo_index, name='index'),
    path('search/',search,name='search'),
    path('add/',create,name='create')
]