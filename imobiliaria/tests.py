from django.test import TestCase
from django.urls import reverse

from .models import Imovel


class ImobiliariaViewsTests(TestCase):
    def setUp(self):
        self.casa = Imovel.objects.create(
            titulo='Casa ensolarada',
            descricao='Uma casa confortável.',
            finalidade=Imovel.Finalidade.VENDA,
            tipo=Imovel.Tipo.CASA,
            cidade='Campinas',
            bairro='Cambuí',
            preco='450000.00',
            area=120,
            quartos=3,
        )
        self.apartamento = Imovel.objects.create(
            titulo='Apartamento central',
            descricao='Perto de tudo.',
            finalidade=Imovel.Finalidade.ALUGUEL,
            tipo=Imovel.Tipo.APARTAMENTO,
            cidade='São Paulo',
            bairro='Centro',
            preco='2500.00',
            area=65,
            quartos=2,
        )

    def test_home_lists_only_active_properties(self):
        self.apartamento.ativo = False
        self.apartamento.save()

        response = self.client.get(reverse('imobiliaria:inicio'))

        self.assertContains(response, self.casa.titulo)
        self.assertNotContains(response, self.apartamento.titulo)

    def test_search_filters_by_city_and_purpose(self):
        response = self.client.get(reverse('imobiliaria:inicio'), {
            'cidade': 'campinas',
            'finalidade': Imovel.Finalidade.VENDA,
        })

        self.assertContains(response, self.casa.titulo)
        self.assertNotContains(response, self.apartamento.titulo)

    def test_search_filters_by_maximum_price(self):
        response = self.client.get(reverse('imobiliaria:inicio'), {'preco_maximo': '3000'})

        self.assertContains(response, self.apartamento.titulo)
        self.assertNotContains(response, self.casa.titulo)

    def test_invalid_maximum_price_does_not_break_listing(self):
        response = self.client.get(reverse('imobiliaria:inicio'), {'preco_maximo': 'NaN'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.casa.titulo)

    def test_detail_page_displays_property(self):
        response = self.client.get(reverse('imobiliaria:detalhe', args=[self.casa.slug]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.casa.titulo)
