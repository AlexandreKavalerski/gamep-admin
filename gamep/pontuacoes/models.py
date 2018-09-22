from django.db import models
from core.models import *

# Create your models here.
class Atividade(models.Model):
    nome = models.CharField(max_length=64)
    alunos = models.ManyToManyField(Aluno, through='AtividadeAluno')

    def __str__(self):
        return self.nome


class AtividadeAluno(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True, blank=True)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE, null=True, blank=True)
    perfeccionismo = models.BooleanField(default=False)
    agilidade = models.BooleanField(default=False)
    precisao = models.BooleanField(default=False)

    def __str__(self):
        return self.aluno.pessoa.nome + ' - ' + self.atividade.nome