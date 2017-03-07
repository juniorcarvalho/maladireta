from django.contrib import admin
from .models import Grupo, Familia, Associado
from .forms import AssociadoForm


class GrupoModelAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


class FamiliaModelAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


class AssociadoModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'familia', 'grupo', 'telefone', 'celular', 'email']
    search_fields = ('nome', 'familia')
    list_filter = ('grupo__nome', 'familia')
    form = AssociadoForm
    fieldsets = [
        (None,
         {'fields': ['nome', 'grupo', 'familia', 'associado']}
         ),
        ('Endereço', {
            'fields': ['cep', ('endereco', 'numero'), ('complemento', 'bairro'),
                       ('cidade', 'uf')]
        }),
        ('Contatos', {
            'fields': ['email', ('telefone', 'celular')]
        })
    ]


admin.site.register(Grupo, GrupoModelAdmin)
admin.site.register(Familia, FamiliaModelAdmin)
admin.site.register(Associado, AssociadoModelAdmin)
