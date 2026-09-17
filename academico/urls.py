from django.urls import path
from .views import listar_turma, adicionar_turma

urlpatterns = [
    path('turmas/', listar_turma, name='listar-turma'),
    path('turmas/adicionar', adicionar_turma, name='adicionar-turma'),
]

