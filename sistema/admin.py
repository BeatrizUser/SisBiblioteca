from django.contrib import admin
from .models import *

@admin.register(CategoriaLivro)
class CategoriaLivroAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editora', 'categoria', 'num_copias_disponiveis', 'status')
    list_filter = ('categoria', 'status')
    search_fields = ('titulo', 'autor', 'isbn')

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'contato')
    search_fields = ('nome', 'matricula', 'contato')

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'pessoa', 'data_emprestimo', 'data_devolucao_prevista', 'data_devolucao_efetiva')
    list_filter = ('data_emprestimo', 'data_devolucao_prevista', 'data_devolucao_efetiva')
    search_fields = ('livro__titulo', 'pessoa__nome', 'pessoa__matricula')

    def save_model(self, request, obj, form, change):
        if not obj.data_devolucao_prevista:
            obj.data_devolucao_prevista = obj.data_emprestimo + timezone.timedelta(days=15)
        obj.save()

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('livro', 'pessoa')

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)