from django.urls import path

from . import views

urlpatterns = [
    # ex: /resultados/
    path('ranking/', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('', views.home, name='home'),
]