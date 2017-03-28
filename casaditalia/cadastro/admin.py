from django.contrib import admin
from django.conf import settings
from .models import Grupo, Familia, Associado, AssociadoFamilia
from .forms import AssociadoForm, FamiliaForm, GrupoForm


class GrupoModelAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    form = GrupoForm

    class Media:
        css = {
            'all': (settings.STATIC_URL + 'css/main.css',)
        }


class FamiliaModelAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    form = FamiliaForm
    ordering = ['nome']

    class Media:
        css = {
            'all': (settings.STATIC_URL + 'css/main.css',)
        }


class AssociadoFamiliaInLine(admin.TabularInline):
    model = AssociadoFamilia
    extra = 1


class AssociadoModelAdmin(admin.ModelAdmin):
    inlines = [AssociadoFamiliaInLine]
    list_display = ['nome', 'grupo', 'telefone', 'celular', 'email']
    search_fields = ('nome',)
    list_filter = ('grupo__nome',)
    form = AssociadoForm
    fieldsets = [
        (None,
         {'fields': ['nome', 'cpf', 'grupo', 'associado']}
         ),
        ('Endereço', {
            'fields': ['cep', ('endereco', 'numero'), ('complemento', 'bairro'),
                       ('cidade', 'uf')]
        }),
        ('Contatos', {
            'fields': ['email', ('telefone', 'celular')]
        })
    ]

    # def familia(self, obj):
    #     return AssociadoFamilia.objects.filter(associado=obj.associado).first()

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.1.1.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.10/jquery.mask.js',
            settings.STATIC_URL + 'js/cadastro.js',
        )
        css = {
            'all': (settings.STATIC_URL + 'css/main.css',)
        }


admin.site.register(Grupo, GrupoModelAdmin)
admin.site.register(Familia, FamiliaModelAdmin)
admin.site.register(Associado, AssociadoModelAdmin)
