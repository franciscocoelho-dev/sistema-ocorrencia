from django.shortcuts import render, redirect, get_object_or_404
from .models import Turma, Aluno
from .forms import TurmaForm, AlunoForm

def listar_turma(request):
    turmas = Turma.objects.all()
    return render(
        request,
        'academico/turmas.html',
        {'context' : turmas}
    )


def adicionar_turma(request):
    if request.method == 'GET':
        form = TurmaForm()
    else: # Então é POST
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listar_turma)
    return render(
        request,
        'academico/add-turmas.html',
        {'form_turma': form}
    )


def visualizar_turma(request, pk):
    turma = get_object_or_404(Turma, pk = pk)
    alunos = Aluno.objects.filter(turma = turma)

    return render(request, 'academico/detalhe-turma.html', {'turma': turma, 'alunos': alunos})


def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(
        request,
        'academico/alunos.html',
        {'context': alunos}
    )


def adicionar_alunos(request):
    if request.method == 'GET':
        form = AlunoForm()
        return render(request, 'academico/add-aluno.html', {'form_aluno': form})
    else:
        # request.method == 'POST'
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(listar_alunos)

