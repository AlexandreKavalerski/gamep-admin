from django.db import models

# Create your models here.
from core.models import Aluno
from pontuacoes.models import AtividadeAluno


class NotasAluno(models.Model):

    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True, blank=True)
    level_precisao = models.IntegerField(null=True, blank=True)
    level_agilidade = models.IntegerField(null=True, blank=True)
    level_perfeccionismo = models.IntegerField(null=True, blank=True)

    def get_slots_precisao(self):
        total_precisao = AtividadeAluno.objects.filter(aluno=self.aluno, precisao=True).count()
        return total_precisao

    def get_slots_agilidade(self):
        total_agilidade = AtividadeAluno.objects.filter(aluno=self.aluno, agilidade=True).count()
        return total_agilidade

    def get_slots_perfeccionismo(self):
        total_perfeccionismo = AtividadeAluno.objects.filter(aluno=self.aluno, perfeccionismo=True).count()
        return total_perfeccionismo

    def get_pontuacao_total(self):
        pontos_agilidade = self.get_slots_agilidade() * 1000
        pontos_perfeccionismo = self.get_slots_perfeccionismo() * 800
        pontos_precisao = self.get_slots_precisao() * 2000

        total_pontos = pontos_agilidade + pontos_perfeccionismo + pontos_precisao
        return total_pontos

