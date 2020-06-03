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

- **Secrety Key**
  - (kvkstore) kvkstore $ heroku config:set DEBUG=False
  - criar file .env -> DEBUG=True
  - criar diretorio contrib- file env-sample -> DEBUG=False
  - gerar uma Secrety key 
  - inserir a secreta-Key no file .env
```
(kvkstore) kvkstore $ python
Python 3.8.0 (default, Feb  3 2020, 16:24:25) 
[GCC 7.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
'secreta-key gerada'
>>> quit()
(kvkstore) kvkstore $ heroku config:set SECRET_KEY='secreta-key gerada'
Setting SECRET_KEY and restarting ⬢ kvkstore... done, v9
SECRET_KEY: secreta-key gerada
```

- **Criar conexão com BD**
  - kvkstore $ pipenv install psycopg2-binary
  - kvkstore $ pipenv install dj-database-url
  - file settings.py
  ```
  default_db_url = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
  parse_database = partial(dj_database_url.parse, conn_max_age=600)
  DATABASES = {
      'default': config('DATABASE_URL', default=default_db_url, cast=parse_database)
  }
  ```

- **Criar app produto**
  - (kvkstore) store $ mng startapp produto
  - kvkstore $ pipenv install xlwt
  - kvkstore $ pipenv install pandas
  - kvkstore $ pipenv install xlrd
  - kvkstore $ pipenv install django-widget-tweaks
  - kvkstore $ pipenv install pytz
  - kvkstore $ pipenv install collectfast

- **criar as migraçoes**
  - (kvkstore) kvkstore $ mng makemigrations
  - (kvkstore) kvkstore $ mng migrate

- **Criado o diretorio fix**
  ```
  fix $ tree
  .
  ├── produtos.csv
  ├── produtos_exportados.csv
  └── produtos.xlsx
  ```