from django.urls import path

from . import views

urlpatterns = [
    # ex: /resultados/
    path('', views.index, name='index'),
]