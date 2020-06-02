# kvkstore

Aplicativo desenvolvido com orientação no projeto estoque (Regis Santos) e tambem baseado no django-blog (Corey Shafer)

![Python application](https://github.com/jlplautz/kvkstore/workflows/Python%20application/badge.svg)
[![Updates](https://pyup.io/repos/github/jlplautz/kvkstore/shield.svg)](https://pyup.io/repos/github/jlplautz/kvkstore/)
[![Python 3](https://pyup.io/repos/github/jlplautz/kvkstore/python-3-shield.svg)](https://pyup.io/repos/github/jlplautz/kvkstore/)

- Estrutura de diretorio Django
```
kvkstore $ tree
.
├── LICENSE
├── Pipfile
├── Pipfile.lock
└── README.md
```

- **Ambiente virtual criado** 
  - pipenv shell
  - source .venv/bin/activate

- **Libs instaladas** 
  - pipenv install -d flake8
  - pipenv install -d pytest-django
  - pipenv install django
  - pipenv install python-decouple

- **Criado projeto Django** 
  - (kvkstore) kvkstore $ django-admin startproject store .
```
(kvkstore) kvkstore $ tree
.
├── LICENSE
├── manage.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── store
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

- **Criado o file .flake8**
```
[flake8]
max-line-length = 120
exclude = .venv
```

- **Criado o file .pyup.yml**

```
requirements:
  - Pipfile
  - Pipfile.lock
```

- **Criado app core**
  - (kvkstore) store $ mng startapp core

- **Lib instalada** 
  - kvkstore $ pipenv install gunicorn


- **Criada app no heroku** 
  - kvkstore $ heroku apps:create kvkstore
  - (kvkstore) kvkstore $ heroku config:set DISABLE_COLLECTSTATIC=1


- **Criado o diretorio core/tests e o file test_home.py** 
```
from django.test import Client
def test_status_code(client:Client):
    resp = client.get('/')
    assert resp.status_code == 200
```