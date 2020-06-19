# from django.test import Client
from store.core.apps import CoreConfig


# def test_status_code(client: Client):
#     """quando accessamos nosso site fazemos uma chamada do tipo get
#     logo na raiz da aplicação. Justamente a view que construimos
#
#     Emulando um request o protocolo http vai retornar um response.
#     Aqui queremos nos certificar que esta resposta retornou com sucesso
#     """
#     resp = client.get('/')
#     assert resp.status_code == 200


def test_core():
    assert CoreConfig.name == 'core'
