from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Oferta
from .forms import OfertaForm

@login_required
def lista_ofertas(request):
    # Filtrar ofertas do usuário logado
    ofertas = Oferta.objects.filter(estabelecimento=request.user)
    
    # Filtro por status
    status_filter = request.GET.get('status')
    if status_filter:
        ofertas = ofertas.filter(status=status_filter)
    
    # Busca por texto
    busca = request.GET.get('busca')
    if busca:
        ofertas = ofertas.filter(
            Q(titulo__icontains=busca) | Q(descricao__icontains=busca)
        )
    
    context = {
        'ofertas': ofertas,
        'status_filter': status_filter or '',
        'busca': busca or '',
    }
    return render(request, 'estabelecimento/lista_ofertas.html', context)

@login_required
def criar_oferta(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST)
        if form.is_valid():
            oferta = form.save(commit=False)
            oferta.estabelecimento = request.user
            oferta.save()
            messages.success(request, 'Oferta criada com sucesso!')
            return redirect('lista_ofertas')
    else:
        form = OfertaForm()
    
    context = {'form': form, 'titulo_pagina': 'Nova Oferta'}
    return render(request, 'estabelecimento/form_oferta.html', context)

@login_required
def editar_oferta(request, id):
    oferta = get_object_or_404(Oferta, id=id, estabelecimento=request.user)
    
    if request.method == 'POST':
        form = OfertaForm(request.POST, instance=oferta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Oferta atualizada com sucesso!')
            return redirect('lista_ofertas')
    else:
        form = OfertaForm(instance=oferta)
    
    context = {'form': form, 'titulo_pagina': 'Editar Oferta', 'editar': True}
    return render(request, 'estabelecimento/form_oferta.html', context)

@login_required
def excluir_oferta(request, id):
    oferta = get_object_or_404(Oferta, id=id, estabelecimento=request.user)
    
    if request.method == 'POST':
        oferta.delete()
        messages.success(request, 'Oferta excluída com sucesso!')
        return redirect('lista_ofertas')
    
    context = {'oferta': oferta}
    return render(request, 'estabelecimento/confirmar_exclusao.html', context)
# Create your views here.
