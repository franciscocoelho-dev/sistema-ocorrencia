
from django import forms
from django.forms import ModelForm
from .models import Turma, Aluno

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'
        widgets = {
            'descricao': forms.TextInput(attrs = {'class': 'form-control'}),
            'ano_letivo': forms.Select(attrs = {'class': 'form-control'}),
        }

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs = {'class': 'form-control'}),
            'cpf': forms.TextInput(attrs = {'class': 'form-control'}),
            'ra': forms.TextInput(attrs = {'class': 'form-control'}),
            'nome_responsavel': forms.TextInput(attrs = {'class': 'form-control'}),
            'telefone_responsavel': forms.TextInput(attrs = {'class': 'form-control'}),
            'turma': forms.Select(attrs = {'class': 'form-control'}),
        }
