from store.users.apps import UsersConfig


def test_test_app_config_name():
    assert UsersConfig.name == 'users'