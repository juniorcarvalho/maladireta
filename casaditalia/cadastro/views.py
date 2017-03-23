from django.shortcuts import render


def relatorioCadastro(request):
    return render(request, 'cadastro/relatoriosCadastro.html')
