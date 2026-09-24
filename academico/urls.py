from django.urls import path
from .views import listar_turma, adicionar_turma, listar_alunos, adicionar_alunos

urlpatterns = [
    path('turmas/', listar_turma, name='listar-turma'),
    path('turmas/adicionar/', adicionar_turma, name='adicionar-turma'),

    path('alunos/', listar_alunos, name='listar-alunos'),
    path('alunos/adicionar/', adicionar_alunos, name='adicionar-alunos'), 
]

