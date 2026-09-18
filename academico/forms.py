
from django import forms
from django.forms import ModelForm
from .models import Turma

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'
        widgets = {
            'descricao': forms.TextInput(attrs = {'class': 'form-control'}),
            'ano_letivo': forms.Select(attrs = {'class': 'form-control'}),
        }
