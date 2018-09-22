from django.contrib import admin
from core.models import *
# Register your models here.


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    raw_id_fields = ('usuario', )


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    search_fields = ('nome_pessoa', )
    list_display = ('nome_pessoa', )
    raw_id_fields = ('pessoa', )

    def nome_pessoa(self, obj):
        return obj.pessoa.nome

    nome_pessoa.admin_order_field = 'pessoa__nome'
    nome_pessoa.__name__ = 'Nome'