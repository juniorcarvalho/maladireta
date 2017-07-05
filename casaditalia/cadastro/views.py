from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import ListaAssociadoForm
from .models import Familia, Associado, AssociadoFamilia, Grupo


def relatorioCadastro(request):
    if request.method == 'POST':
        select = request.POST['selectFamilia']
        familias = Familia.objects.all().order_by('nome')
        familiaSelect = Familia.objects.get(pk=select)
        af = AssociadoFamilia.objects.filter(familia=familiaSelect).values_list('associado')
        listaAssociado = Associado.objects.filter(pk__in=af)
        context = {}
        context['familias'] = familias
        context['lista'] = listaAssociado
        return render(request, 'cadastro/relatoriosCadastro.html', context)

    if request.method == 'GET':
        familias = Familia.objects.all().order_by('nome')
        return render(request, 'cadastro/relatoriosCadastro.html', {'familias': familias})
        # form = ListaAssociadoForm()
        # return HttpResponse(form)


def etiquetaAssociado(request):
    if request.method == 'GET':
        grupos = Grupo.objects.all().order_by('nome')
        return render(request, 'cadastro/etiquetaAssociado.html', {'grupos': grupos})


def etiquetaPrint(request, pkGrupo):
    grupo = Grupo.objects.get(pk=pkGrupo)
    associados = Associado.objects.all(grupo=grupo)
    return render(request, 'cadastro/etiquetaPrint.html', {'associados': associados})
    pass
