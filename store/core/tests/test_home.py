from django.test import Client


def test_status_code(client: Client):
    """quando accessamos nosso site fazemos uma chamada do tipo get
    logo na raiz da aplicação. Justamente a view que construimos

    Emulando um request o protocolo http vai retornar um response.
    Aqui queremos nos certificar que esta resposta retornou com sucesso
    """
    resp = client.get('/')
    assert resp.status_code == 200
