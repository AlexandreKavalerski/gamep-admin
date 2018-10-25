from django.urls import path

from . import views

urlpatterns = [
    # ex: /resultados/
    path('ranking/', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('sobre/', views.sobre, name='sobre'),
    path('', views.home, name='home'),
]