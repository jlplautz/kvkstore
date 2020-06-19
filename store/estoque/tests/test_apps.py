from store.estoque.apps import EstoqueConfig


def test_estoque():
    assert EstoqueConfig.name == 'estoque'
