from django.contrib import admin

from .models import Cliente, Funcionario, Imovel, Locacao, Ocorrencia

admin.site.register(Funcionario)
admin.site.register(Imovel)
admin.site.register(Cliente)
admin.site.register(Locacao)
admin.site.register(Ocorrencia)
