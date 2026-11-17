from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe

from .models import Funcionario


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
