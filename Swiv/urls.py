from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book , name='book'),
    path('payment/', views.redirecttopayment, name='payment'),
    path('', views.register, name='register'),
    path('login', views.user_login , name='login'),
    path('lipa/', views.lipa , name='lipa' ),
    path('callback/', views.callback , name='callback'),
    path('logout/', views.logout_view , name="logout")
]
