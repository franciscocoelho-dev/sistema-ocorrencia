from django.contrib import admin
from .models import AnoLetivo,Turma,Aluno, Ocorrencia

admin.site.register(AnoLetivo)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Ocorrencia)

