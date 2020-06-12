from store.produto.apps import ProdutoConfig


def test_produto():
    assert ProdutoConfig.name == 'produto'
