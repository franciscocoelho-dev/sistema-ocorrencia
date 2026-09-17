from django.urls import path
from .views import listar_turma

urlpatterns = [
    path('turmas/', listar_turma, name='listar-turma')
]

