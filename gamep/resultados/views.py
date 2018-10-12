from django.http import Http404
from django.shortcuts import render

# Create your views here.
from core.models import Aluno
from .models import *

def index(request):
    try:
        alunos = Aluno.objects.all()
        totais = []
        for aluno in alunos:
            try:
                tot = NotasAluno.objects.get(aluno=aluno)
            except NotasAluno.DoesNotExist:
                NotasAluno.objects.create(aluno=aluno).save()
                tot = NotasAluno.objects.get(aluno=aluno)

            aluno.slots_precisao = tot.get_slots_precisao()
            aluno.slots_agilidade = tot.get_slots_agilidade()
            aluno.slots_perfeccionismo = tot.get_slots_perfeccionismo()
            aluno.total_de_pontos = tot.get_pontuacao_total()


    except Aluno.DoesNotExist:
        raise Http404("Nenhum aluno encontrado")
    return render(request, 'resultados/ranking.html', {'alunos': alunos})


