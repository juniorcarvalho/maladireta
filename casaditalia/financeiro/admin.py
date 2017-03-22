from django.contrib import admin
#from .models import Receber
from .forms import ReceberForm
from django.conf import settings


class ReceberModelAdmin(admin.ModelAdmin):
    list_display = ['associado', 'ano_ref', 'valor', 'data_ven', 'data_pag']
    search_fields = ['associado', 'ano_ref']
    list_filter = ['associado', 'ano_ref', 'data_pag']

    form = ReceberForm

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.1.1.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.10/jquery.mask.js',
            settings.STATIC_URL + 'js/receber.js',
        )


#admin.site.register(Receber, ReceberModelAdmin)
