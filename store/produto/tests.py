from store.produto.apps import ProdutoConfig


def test_test_app_config_name():
    assert ProdutoConfig.name == 'produto'