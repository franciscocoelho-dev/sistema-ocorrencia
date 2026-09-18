from django.shortcuts import render, redirect
from .models import Turma
from .forms import TurmaForm

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

