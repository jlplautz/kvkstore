from store.estoque.apps import EstoqueConfig


def test_app_config_name():
    assert EstoqueConfig.name == 'estoque'