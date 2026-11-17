from django.contrib.auth.models import User
from django.db import models


class Funcionario(models.Model):
    CARGO_CHOICES = [
        ('corretor', 'Corretor'),
        ('gerente', 'Gerente'),
        ('administracao', 'Administração'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['usuario__first_name', 'usuario__last_name', 'usuario__username']

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username
