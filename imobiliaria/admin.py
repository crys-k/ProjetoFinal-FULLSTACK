from django.contrib import admin

from .models import Imovel


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cidade', 'bairro', 'finalidade', 'tipo', 'preco', 'ativo', 'destaque')
    list_filter = ('ativo', 'destaque', 'finalidade', 'tipo', 'cidade')
    search_fields = ('titulo', 'cidade', 'bairro')
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ('-destaque', '-criado_em')
