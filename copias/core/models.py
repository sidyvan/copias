from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

PAPEL = (
    ('A4', 'A4'),
    ('A3', 'A3'),

)
class Preco(models.Model):
    criado_em = models.DateTimeField('Criado em',auto_now_add=True)
    data = models.DateField('data',auto_now_add=True)
    editao_em = models.DateTimeField('Editado em',auto_now=True)
    titulo = models.CharField('Descrição',max_length=100)
    colorido = models.BooleanField('Colorido',default=False)
    papel = models.CharField('Papel',default='A4',choices=PAPEL, max_length=10)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    valor_copia = models.DecimalField('Valor por cópia',max_digits=8, decimal_places=2)

    def __str__(self):
        return self.titulo


class Contador(models.Model):
    criado_em = models.DateTimeField('Criado em',auto_now_add=True)
    numero =  models.PositiveIntegerField()
    def __unicode__(self):
        return self.numero

class Caixa(models.Model):

    data_hora = models.DateTimeField('Criado em',auto_now_add=True)
    criado_em = models.DateField('data',auto_now_add=True)
    quantidade = models.PositiveIntegerField('Quantidade de Cópias',default=1)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    preco = models.ForeignKey(Preco, on_delete=models.CASCADE, default='Aluno - Preto / Branco - 0,10')

    valor_total = models.DecimalField('Valor Total',max_digits=8, decimal_places=2)


    def __unicode__(self):
        return self.quantidade
