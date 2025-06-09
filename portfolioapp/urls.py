from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('header/', views.header, name='header'),
    path('about/', views.about_me, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('education/', views.education, name='education'),
]