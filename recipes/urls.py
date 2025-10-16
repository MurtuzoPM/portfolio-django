from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('tags/<slug:slug>/', views.tag, name='tag'),
    path('recipes/<slug:slug>/', views.detail, name='detail'),
]
