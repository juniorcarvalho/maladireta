from django.forms import ModelForm, TextInput, Select
from django import forms
from .models import Receber


class ReceberForm(ModelForm):
    class Meta:

        widgets = {
            'associado': Select(attrs={'class': 'input-xxlarge'}),
            'ano_ref': TextInput(attrs={'class': 'input-small'}),
            'valor': TextInput(attrs={'class': 'input-small'}),
        }

    def clean(self):
        nosso_numero_old = self.instance.nosso_numero
        nosso_numero_new = self.cleaned_data.get('nosso_numero')
        if nosso_numero_new != None:
            if len(nosso_numero_new) > 0:
                if Receber.objects.filter(nosso_numero=nosso_numero_new).exclude(
                        nosso_numero=nosso_numero_old).exists():
                    raise forms.ValidationError('Nosso número já cadastrado')
        return self.cleaned_data
