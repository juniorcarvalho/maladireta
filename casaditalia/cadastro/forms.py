from django.forms import ModelForm, TextInput
from django import forms
from .models import Associado, Familia, Grupo
from .cpf import CPF


class AssociadoForm(ModelForm):
    class Meta:
        model = Associado
        fields = ['nome', 'cpf', 'grupo', 'associado', 'cep',
                  'endereco', 'numero', 'complemento', 'bairro', 'cidade',
                  'uf', 'email', 'telefone', 'celular']
        widgets = {
            'nome': TextInput(attrs={'class': 'input-xxlarge'}),
            'cep': TextInput(attrs={'class': 'input-small'}),
            'numero': TextInput(attrs={'class': 'input-small'}),
            'uf': TextInput(attrs={'class': 'input-small'}),
            'email': TextInput(attrs={'class': 'input-xxlarge'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if not CPF(cpf).isValid():
            raise forms.ValidationError('CPF inválido')
        return self.cleaned_data['cpf']

    def clean_nome(self):
        return self.cleaned_data.get('nome').upper()

    def clean_endereco(self):
        return self.cleaned_data.get('endereco').upper()

    def clean_complemento(self):
        return self.cleaned_data.get('complemento').upper()

    def clean_bairro(self):
        return self.cleaned_data.get('bairro').upper()

    def clean_cidade(self):
        return self.cleaned_data.get('cidade').upper()

    def clean_uf(self):
        return self.cleaned_data.get('uf').upper()

    def clean_email(self):
        email_old = self.instance.email
        email_new = self.cleaned_data.get('email')
        if len(email_new) > 0:
            if Associado.objects.filter(email=email_new).exclude(email=email_old).exists():
                raise forms.ValidationError('Email já cadastrado')
        return self.cleaned_data['email']

        # def clean(self):
        #     #associado = self.cleaned_data.get('associado')
        #     #cpf_old = self.instance.cpf
        #     #cpf_new = self.cleaned_data.get('cpf')
        #     email_old = self.instance.email
        #     email_new = self.cleaned_data.get('email')
        #
        #     # validando cpf
        #     # se for associado, obrigatório informar CPF
        #     # if associado and len(cpf_new) == 0:
        #     #     raise forms.ValidationError('Obrigatório informar CPF para associado.')
        #
        #     # se for associado e informou cpf, verifica duplicidade
        #     # if len(cpf_new) > 0:
        #     #     if Associado.objects.filter(cpf=cpf_new).exclude(cpf=cpf_old).exists():
        #     #         raise forms.ValidationError('CPF já cadastrado')
        #
        #     # validando email
        #     # se informou email, verifica duplicidade
        #     if len(email_new) > 0:
        #         if Associado.objects.filter(email=email_new).exclude(email=email_old).exists():
        #             raise forms.ValidationError('Email já cadastrado')
        #
        #     return self.cleaned_data


class FamiliaForm(ModelForm):
    class Meta:
        model = Familia
        fields = ['nome']

    def clean_nome(self):
        return self.cleaned_data.get('nome').upper()


class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome']

    def clean_nome(self):
        return self.cleaned_data.get('nome').upper()


# class ListaAssociadoForm(forms.Form):
#
#     familias = forms.ModelChoiceField(queryset=Familia.objects.all().order_by('nome'),
#                                       required=True, label='Famílias', empty_label=None,
#                                       widget=forms.Select(attrs={'class': 'selectpicker'})
#                                       )
