from django.contrib import admin
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from core.models import *

# Register your models here.


class AtividadeAlunoInline(admin.TabularInline):
    model = AtividadeAluno
    extra = 0
    # raw_id_fields = ('aluno',)
    fields = ('nome_aluno', 'perfeccionismo', 'agilidade', 'precisao')
    readonly_fields = ('nome_aluno', )

    def nome_aluno(self, obj):
        return obj.aluno.pessoa.nome

    nome_aluno.admin_order_field = 'aluno__pessoa__nome'
    nome_aluno.__name__ = 'Nome do Aluno'

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', )
    inlines = (AtividadeAlunoInline, )
    change_form_template = 'admin/atividade_change_form.html'

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            path(
                '<pk>/carregar-alunos',
                self.admin_site.admin_view(self.carregar_dados_alunos),
                name='core_acao_carregar_dados_alunos'
            ), ]
        return custom_urls + urls

    def carregar_dados_alunos(self, request, pk, *args, **kwargs):
        try:
            atividade = Atividade.objects.get(pk=pk)
            alunos = Aluno.objects.all().order_by('pessoa__nome') #futuramente filtrar de acordo com a turma
            for aluno in alunos:
                atividade_aluno, created = AtividadeAluno.objects.get_or_create(
                    atividade=atividade,
                    aluno=aluno
                )

        except Exception as e:
            self.message_user(request,
                              'Problemas ao carregar os alunos. Entre em contato com os desenvolvedores ',
                              level=messages.ERROR)
        self.message_user(request, 'Participantes atualizados com successo')
        return HttpResponseRedirect(
            reverse('admin:pontuacoes_atividade_change', args=[pk])
        )
