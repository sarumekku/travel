from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.demo1, name="demo1"),

    #path('about/', views.about, name='about'),
    #path('menu/', views.menu, name='menu'),
    #path('thanks/', views.thanks, name='thank')
    #path('add/',views.addition,name='addition')
]
