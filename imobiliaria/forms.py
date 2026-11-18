from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.utils.safestring import mark_safe

from .models import Cliente, FotoImovel, Funcionario, Imovel, Locacao, Ocorrencia


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
        fields = ['endereco', 'tipo', 'quartos', 'metragem', 'valor_aluguel']

    def clean_valor_aluguel(self):
        valor_aluguel = self.cleaned_data['valor_aluguel']
        if valor_aluguel <= 0:
            raise forms.ValidationError('O valor do aluguel deve ser maior que zero.')
        return valor_aluguel


class PesquisaImovelForm(forms.Form):
    endereco = forms.CharField(required=False, label='Endereço')
    tipo = forms.ChoiceField(choices=[('', 'Todos os tipos')] + Imovel.TIPO_CHOICES, required=False, label='Tipo')
    quartos_min = forms.IntegerField(required=False, label='Quartos (mínimo)')
    valor_min = forms.DecimalField(required=False, label='Valor mínimo')
    valor_max = forms.DecimalField(required=False, label='Valor máximo')


class FotoImovelForm(forms.ModelForm):
    class Meta:
        model = FotoImovel
        fields = ['imagem']
        labels = {'imagem': 'Foto'}

    def clean_imagem(self):
        imagem = self.cleaned_data['imagem']
        if imagem.size > 5 * 1024 * 1024:
            raise forms.ValidationError('A imagem deve ter no máximo 5 MB.')
        return imagem


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


class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['imovel', 'descricao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imovel'].queryset = Imovel.objects.filter(ativo=True)
