from django.shortcuts import render
from .models import Familia


def relatorioCadastro(request):
    familias = Familia.objects.all().order_by('nome')
    return render(request, 'cadastro/relatoriosCadastro.html', {'familias': familias})
