from django.db import models
from datetime import datetime

class AnoLetivo(models.Model):
    ano = models.IntegerField(default=datetime.now().year)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.ano)

class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=75, verbose_name='Descrição')
    ano_letivo = models.ForeignKey(
        AnoLetivo, 
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.descricao

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    ra = models.CharField(max_length=11, verbose_name='R.A.')
    nome_responsavel = models.CharField(max_length=50, verbose_name='Nome do Responsável')
    telefone_responsavel = models.CharField(max_length=20, verbose_name='Telefone do Responsável')
    turma = models.ForeignKey(
        Turma,
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return self.nome


class Ocorrencia(models.Model):
    GRAVIDADE_CHOICES = (
        ('L', 'Leve'),
        ('M', 'Moderada'),
        ('G', 'Grave'),
    )

    id = models.AutoField(primary_key=True)
    descricao = models.TextField()
    gravidade = models.CharField(max_length=1, choices=GRAVIDADE_CHOICES, default='L')
    aluno = models.ManyToManyField(Aluno, related_name='ocorrencias')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.descricao


