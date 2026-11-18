from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.utils.safestring import mark_safe

from .models import Cliente, Funcionario, Imovel, Locacao


class UsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Nome'
        self.fields['last_name'].label = 'Sobrenome'
        self.order_fields(['first_name', 'last_name', 'username', 'password1', 'password2'])
        self.fields['password1'].help_text = mark_safe(
            '<ul>'
            '<li>Não pode ser muito parecida com as suas outras informações pessoais.</li>'
            '<li>Precisa conter pelo menos 8 caracteres.</li>'
            '<li>Não pode ser uma senha comumente utilizada.</li>'
            '<li>Não pode ser inteiramente numérica.</li>'
            '</ul>'
        )


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['cargo', 'telefone']


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['endereco', 'tipo', 'quartos', 'metragem', 'valor_aluguel', 'foto']

    def clean_valor_aluguel(self):
        valor_aluguel = self.cleaned_data['valor_aluguel']
        if valor_aluguel <= 0:
            raise forms.ValidationError('O valor do aluguel deve ser maior que zero.')
        return valor_aluguel


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf_cnpj', 'telefone', 'endereco']
        labels = {'cpf_cnpj': 'CPF/CNPJ'}

    def clean_cpf_cnpj(self):
        cpf_cnpj = self.cleaned_data['cpf_cnpj']
        somente_digitos = ''.join(caractere for caractere in cpf_cnpj if caractere.isdigit())

        if len(somente_digitos) not in (11, 14):
            raise forms.ValidationError('Informe um CPF (11 dígitos) ou CNPJ (14 dígitos) válido.')

        clientes_existentes = Cliente.objects.filter(cpf_cnpj=somente_digitos)
        if self.instance.pk:
            clientes_existentes = clientes_existentes.exclude(pk=self.instance.pk)
        if clientes_existentes.exists():
            raise forms.ValidationError('Já existe um cliente cadastrado com este CPF/CNPJ.')

        return somente_digitos


class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['cliente', 'imovel', 'data_inicio', 'data_fim_prevista']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim_prevista': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, busca=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imovel'].queryset = Imovel.objects.filter(status='disponivel', ativo=True)
        clientes = Cliente.objects.all()
        if busca:
            clientes = clientes.filter(Q(nome__icontains=busca) | Q(cpf_cnpj__icontains=busca))
        self.fields['cliente'].queryset = clientes

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim_prevista = cleaned_data.get('data_fim_prevista')
        if data_inicio and data_fim_prevista and data_fim_prevista <= data_inicio:
            raise forms.ValidationError('A data de fim prevista deve ser posterior à data de início.')
        return cleaned_data
