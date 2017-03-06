from django.forms import ModelForm, TextInput


class AssociadoForm(ModelForm):
    class Meta:
        widgets = {
            'nome': TextInput(attrs={'class': 'input-xxlarge'}),
            'cep': TextInput(attrs={'class': 'input-small'}),
            'numero': TextInput(attrs={'class': 'input-small'}),
            'uf': TextInput(attrs={'class': 'input-small'}),
            'email': TextInput(attrs={'class': 'input-xxlarge'}),
        }
