from django.contrib import admin
from django.urls import path

from Academia.views import listaClientes, AlunoView

urlpatterns = [
    path('outro/', listaClientes),
    path('alunos', AlunoView.as_view())
]