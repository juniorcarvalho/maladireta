from django.forms import ModelForm, TextInput, Select
from .models import Receber


class ReceberForm(ModelForm):
    class Meta:

        widgets = {
            'associado': Select(attrs={'class': 'input-xxlarge'}),
            'ano_ref': TextInput(attrs={'class': 'input-small'}),
            'valor': TextInput(attrs={'class': 'input-small'}),
            'data_doc': TextInput(attrs={'class': 'input-small'}),
            'data_ven': TextInput(attrs={'class': 'input-small'}),
            'data_pag': TextInput(attrs={'class': 'input-small'}),
        }
