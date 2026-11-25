from django.shortcuts import render

from .models import (
    Categoria,  # noqa: F401
    Cliente,  # noqa: F401
    Endereco,  # noqa: F401
    ItemEstoque,  # noqa: F401
    ItemPedido,  # noqa: F401
    Pedido,  # noqa: F401
    Produto,
    Tipo,  # noqa: F401
)


def homepage(request):
    return render(request, "homepage.html")


def loja(request):
    produtos = Produto.objects.all()
    context = {
        "produtos": produtos,
    }
    return render(request, "loja.html", context=context)


def carrinho(request):
    return render(request, "carrinho.html")


def checkout(request):
    return render(request, "checkout.html")


def minha_conta(request):
    return render(request, "usuario/minha_conta.html")


def login(request):
    return render(request, "usuario/login.html")
