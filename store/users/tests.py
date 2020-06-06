from store.users.apps import UsersConfig


def test_users():
    assert UsersConfig.name == 'users'