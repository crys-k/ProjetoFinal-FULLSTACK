from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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
    motivo_bloqueio = models.CharField(max_length=255, blank=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f'{self.endereco} ({self.get_tipo_display()})'

    @property
    def pode_bloquear(self):
        return not self.locacao_set.filter(status='ativa').exists()

    def bloquear(self, motivo):
        if not self.pode_bloquear:
            return
        self.status = 'indisponivel'
        self.motivo_bloqueio = motivo
        self.save()

    def desbloquear(self):
        self.status = 'disponivel'
        self.motivo_bloqueio = ''
        self.save()


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


class Locacao(models.Model):
    STATUS_CHOICES = [
        ('ativa', 'Ativa'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    imovel = models.ForeignKey(Imovel, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, null=True)
    data_inicio = models.DateField()
    data_fim_prevista = models.DateField()
    data_fim_real = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativa')
    motivo_cancelamento = models.CharField(max_length=255, blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criada_em']

    def __str__(self):
        return f'{self.cliente} - {self.imovel} ({self.data_inicio} a {self.data_fim_prevista})'

    @property
    def pode_finalizar(self):
        return self.status == 'ativa'

    @property
    def pode_cancelar(self):
        return self.status == 'ativa' and self.data_inicio > timezone.now().date()

    def finalizar(self):
        if not self.pode_finalizar:
            return
        self.data_fim_real = timezone.now().date()
        self.status = 'finalizada'
        self.save()
        self.imovel.status = 'disponivel'
        self.imovel.save()

    def cancelar(self, motivo):
        if not self.pode_cancelar:
            return
        self.status = 'cancelada'
        self.motivo_cancelamento = motivo
        self.save()
        self.imovel.status = 'disponivel'
        self.imovel.save()
