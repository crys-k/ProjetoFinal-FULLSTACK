from django.db import models


SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
    ('N', 'Não Informar'),
]

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    sexo =  models.CharField(max_length=1,choices=SEXO_CHOICES)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    
    def save(self, *args, **kwargs): 
        self.nome = self.nome.title()
        self.sobrenome = self.sobrenome.title()
        self.email = self.email.lower()
        
        super().save(*args, **kwargs)
