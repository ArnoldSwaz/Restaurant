from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
]
