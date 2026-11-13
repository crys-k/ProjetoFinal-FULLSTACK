from django import forms
from .models import Funcionario

class funcionarioForm(forms.ModelForm):
    class Meta: 
        model = Funcionario
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'sexo', 'ativo']
        