from django.db import models
from casaditalia.cadastro.models import Associado
from django.core import validators
import re


class Receber(models.Model):
    associado = models.ForeignKey(Associado)
    ano_ref = models.CharField('Ano Referência', max_length=4, validators=[
        validators.RegexValidator(
            re.compile('^\d{4}$'),
            'Informe apenas números.',
            'invalid'
        )
    ])
    data_doc = models.DateField('Data Documento')
    data_ven = models.DateField('Data Vencimento')
    data_pag = models.DateField('Data Pagamento', null=True, blank=True)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=9)
    observacoes = models.TextField('Observações', max_length=500, null=True, blank=True)
    nosso_numero = models.CharField('Nosso Nro.', max_length=20, null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Contas a Receber'
        verbose_name_plural = 'Contas a Receber'

    def __str__(self):
        return self.ano_ref


