from django.db import models
import re
from django.core import validators


class Familia(models.Model):
    nome = models.CharField('Nome', max_length=50, unique=True)

    class Meta:
        verbose_name = 'família'
        verbose_name_plural = 'famílias'

    def __str__(self):
        return self.nome


class Grupo(models.Model):
    nome = models.CharField('Grupo', max_length=50, unique=True)

    class Meta:
        verbose_name = 'grupo'
        verbose_name_plural = 'grupos'

    def __str__(self):
        return self.nome


class Associado(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=14, unique=True, validators=[
        validators.RegexValidator(
            re.compile('^\d{3}.\d{3}.\d{3}-\d{2}$'),
            'Informe o CPF no formato xxx.xxx.xxx-xx',
            'invalid'
        )
    ])
    grupo = models.ForeignKey(Grupo)
    associado = models.BooleanField('Contribuinte')
    cep = models.CharField('CEP', max_length=9, blank=True, null=True, validators=[
        validators.RegexValidator(
            re.compile('^\d{5}-\d{3}$'),
            'Informe o CEP no formado xxxxx-xxx.',
            'invalid'
        )
    ])
    endereco = models.CharField('Endereço', max_length=100, blank=True, null=True)
    numero = models.CharField('Número', max_length=10, blank=True, null=True)
    complemento = models.CharField('Complemento', max_length=50, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=50, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=50, blank=True, null=True)
    uf = models.CharField('UF', max_length=2, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=15, blank=True, null=True,
                                validators=[
                                    validators.RegexValidator(
                                        re.compile('^\d{2}-\d{4}-\d{4}$'),
                                        'Informe o TELEFONE no formato xx-xxxx-xxxx',
                                        'invalid'
                                    )
                                ])
    celular = models.CharField('Celular', max_length=15, blank=True, null=True,
                               validators=[
                                   validators.RegexValidator(
                                       re.compile('^\d{2}-\d{5}-\d{4}$'),
                                       'Informe o CELULAR no formato xx-xxxxx-xxxx',
                                       'invalid'
                                   )
                               ]
                               )

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'associado'
        verbose_name_plural = 'associados'

    def __str__(self):
        return self.nome


class AssociadoFamilia(models.Model):
    associado = models.ForeignKey(Associado, verbose_name='associado',
                                  on_delete=models.CASCADE)

    familia = models.ForeignKey(Familia, verbose_name='familia')

    class Meta:
        verbose_name = 'família'
        verbose_name_plural = 'famílias'
        unique_together = (('associado', 'familia'))

    def __str__(self):
        return self.familia.nome
