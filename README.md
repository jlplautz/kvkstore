# kvkstore

Aplicativo desenvolvido com orientação no projeto estoque (Regis Santos) e tambem baseado no django-blog (Corey Shafer)


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
