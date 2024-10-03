from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import ProdutoForm, ClienteForm, ComprasForm
from .models import Produto, Cliente, Compras
from django.contrib import messages


def home(response):
    return render(response,'index.html')


def cadastrarProdutos(response):
    form = ProdutoForm()
    context = {'form': form}
    return render(response, 'cadastroProdutos.html', context)

 
def cadastrarClientes(response):
    form = ClienteForm()
    context = {'form': form}
    return render(response, 'cadastroCliente.html', context)


def cadastrarCompras(response):
    form = ComprasForm()
    context = {'form': form}
    return render(response, 'cadastroCompras.html', context)


def mostrarProdutos(response):
    produto = Produto.objects.all()
    context = {'mostrarProdutos': produto}
    return render(response, 'mostrarProdutos.html', context)


def mostrarClientes(response):
    cliente = Cliente.objects.all()
    context = {'mostrarClientes': cliente}
    return render(response, 'mostrarClientes.html', context)


def mostrarCompras(response):
    compras = Compras.objects.all()
    context = {'mostrarCompras': compras}
    return render(response, 'mostrarCompras.html', context)


def cadastrarProdutosEvent(response):
    if response.method == 'POST':
        form = ProdutoForm(response.POST, response.FILES)
        if form.is_valid():
            produto = form.save()
            mensagem = "Produto cadastrado com sucesso!"
            return render(response, 'sucessoCadastro.html', {'mensagem': mensagem})
        mensagemErro = "Erro! Preencha os dados corretamente."
        return render(response, 'semSucessoCadastro.html', {'mensagem': mensagemErro})

    form = ProdutoForm()
    return render(response, 'cadastroProdutos.html', {'form': form})


def cadastrarClientesEvent(response):
    if response.method == 'POST':
        form = ClienteForm(response.POST)
        if form.is_valid():
            cliente = form.save()
            mensagem = "Cliente cadastrado com sucesso!"
            return render(response, 'sucessoCadastro.html', {'mensagem': mensagem})
        mensagemErro = "Erro! Preencha os dados corretamente."
        return render(response, 'semSucessoCadastro.html', {'mensagem': mensagemErro})

    form = ClienteForm()
    return render(response, 'cadastroCliente.html', {'form': form})


def cadastrarComprasEvent(response):
    if response.method == 'POST':
        form = ComprasForm(response.POST)
        if form.is_valid():
            compras = form.save()
            mensagem = "Compra cadastrada com sucesso!"
            return render(response, 'sucessoCadastro.html', {'mensagem': mensagem})
    mensagemErro = "Erro! Preencha os dados corretamente."
    return render(response, 'semSucessoCadastro.html', {'mensagem': mensagemErro})


def marcar_pagamento(response, id):
    compra = get_object_or_404(Compras, id=id)
    compra.pagamento = True
    compra.save()
    return redirect('/mostrarCompras/')


def erroEstoqueInsuficiente(response):
    return render(response, 'erroEstoque.html')


def produtoSucesso(response):
    mensagem = "Produto cadastrado com sucesso!"
    return render(response, 'sucessoCadastro.html', {'mensagem': mensagem})


def clienteSucesso(response):
    mensagem = "Cliente cadastrado com sucesso!"
    return render(response, 'sucessoCadastro.html', {'mensagem': mensagem})


def compraSucesso(response):
    mensagem = "Compra cadastrada com sucesso!"
    return render(response, 'sucessoCadastro.html', {'mensagem': mensagem})


def produtoFalha(response):
    mensagem = "Erro! Preencha os dados corretamente."
    return render(response, 'semSucessoCadastro.html', {'mensagem': mensagem})


def clienteFalha(response):
    mensagem = "Erro! Preencha os dados corretamente."
    return render(response, 'semSucessoCadastro.html', {'mensagem': mensagem})


def compraFalha(response):
    mensagem = "Erro! Preencha os dados corretamente."
    return render(response, 'semSucessoCadastro.html', {'mensagem': mensagem})


def editarProdutos(response, id):
    produto = get_object_or_404(Produto, id=id)
    if response.method == 'POST':
        form = ProdutoForm(response.POST, response.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(response, 'Produto atualizado com sucesso!')
            return redirect('mostrarProdutos')
    else:
        form = ProdutoForm(instance=produto)
    return render(response, 'editarProdutos.html', {'form': form, 'produto': produto})


def editarClientes(response, id):
    cliente = get_object_or_404(Cliente, id=id)
    if response.method == 'POST':
        form = ClienteForm(response.POST, response.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(response, 'Cliente atualizado com sucesso!')
            return redirect('mostrarClientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(response, 'editarClientes.html', {'form': form, 'cliente': cliente})


def editarCompras(response, id):
    compra = get_object_or_404(Compras, id=id)
    if response.method == 'POST':
        form = ComprasForm(response.POST, response.FILES, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(response, 'Compra atualizada com sucesso!')
            return redirect('mostrarCompras')
    else:
        form = ComprasForm(instance=compra)
    return render(response, 'editarCompras.html', {'form': form, 'compra': compra})


def deletarCliente(response, id):
    cliente = get_object_or_404(Cliente, id=id)
    if response.method == "POST":
        cliente.delete()
        return redirect('mostrarClientes')
    return render(response, 'deletarCliente.html', {'cliente': cliente})


def deletarProduto(response, id):
    produto = get_object_or_404(Produto, id=id)
    if response.method == "POST":
        produto.delete()
        return redirect('mostrarProdutos')
    return render(response, 'deletarProduto.html', {'produto': produto})


def deletarCompra(response, id):
    compra = get_object_or_404(Compras, id=id)
    if response.method == "POST":
        compra.delete()
        return redirect('mostrarCompras')
    return render(response, 'deletarCompra.html', {'compra': compra})