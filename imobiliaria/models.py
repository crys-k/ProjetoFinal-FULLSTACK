from django.db import models
from django.utils.text import slugify


class Imovel(models.Model):
    class Finalidade(models.TextChoices):
        VENDA = 'venda', 'Comprar'
        ALUGUEL = 'aluguel', 'Alugar'

    class Tipo(models.TextChoices):
        CASA = 'casa', 'Casa'
        APARTAMENTO = 'apartamento', 'Apartamento'
        TERRENO = 'terreno', 'Terreno'
        COMERCIAL = 'comercial', 'Comercial'

    titulo = models.CharField('título', max_length=140)
    slug = models.SlugField('endereço amigável', max_length=160, unique=True, blank=True)
    descricao = models.TextField('descrição')
    finalidade = models.CharField('finalidade', max_length=10, choices=Finalidade.choices)
    tipo = models.CharField('tipo de imóvel', max_length=20, choices=Tipo.choices)
    cidade = models.CharField('cidade', max_length=100)
    bairro = models.CharField('bairro', max_length=100)
    preco = models.DecimalField('preço', max_digits=12, decimal_places=2)
    area = models.PositiveIntegerField('área (m²)')
    quartos = models.PositiveSmallIntegerField('quartos', default=0)
    banheiros = models.PositiveSmallIntegerField('banheiros', default=0)
    vagas = models.PositiveSmallIntegerField('vagas', default=0)
    imagem_url = models.URLField('URL da imagem', blank=True)
    destaque = models.BooleanField('destacar na página inicial', default=False)
    ativo = models.BooleanField('publicado', default=True)
    criado_em = models.DateTimeField('cadastrado em', auto_now_add=True)

    class Meta:
        ordering = ['-destaque', '-criado_em']
        verbose_name = 'imóvel'
        verbose_name_plural = 'imóveis'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titulo) or 'imovel'
            slug = base_slug
            suffix = 2
            while Imovel.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base_slug}-{suffix}'
                suffix += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
