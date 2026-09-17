from django.shortcuts import render
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
    form = TurmaForm()
    return render(
        request,
        'academico/add-turmas.html',
        {'form_turma': form}
    )

