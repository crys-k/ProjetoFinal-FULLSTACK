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


class Imovel(models.Model):
    TIPO_CHOICES = [
        ('apartamento', 'Apartamento'),
        ('casa', 'Casa'),
        ('sala_comercial', 'Sala comercial'),
    ]

    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('alugado', 'Alugado'),
        ('indisponivel', 'Indisponível'),
    ]

    endereco = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    quartos = models.PositiveSmallIntegerField()
    metragem = models.DecimalField(max_digits=6, decimal_places=2)
    valor_aluguel = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.endereco} ({self.get_tipo_display()})'


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.cpf_cnpj})'

    def save(self, *args, **kwargs):
        self.nome = self.nome.title()
        super().save(*args, **kwargs)
