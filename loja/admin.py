from django.contrib import admin

from .models import (
    Categoria,
    Cliente,
    Endereco,
    ItemEstoque,
    ItemPedido,
    Pedido,
    Produto,
    Tipo,
)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemEstoque)
class ItemEstoqueAdmin(admin.ModelAdmin):
    pass


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    pass


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    pass


@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    pass
