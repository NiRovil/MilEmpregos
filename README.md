# MilEmpregos 
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/NiRovil/Teste-PythonDjango/blob/main/LICENSE) 

### Sobre o projeto

O projeto MilEmpregos é uma aplicação web, construída em Python, usando o framework Django.

A aplicação consiste na criação e divulgação de vagas de emprego, tal qual, a inscrição de candidatos nessas vagas.

# Tecnologias utilizadas
### Back end
- Python
- Django
### Front end
- HTML / CSS 

# Recursos

- Cadastrar usuários (candidatos e empresas);
- Autenticação e login;
- Cadastrar/deletar vagas;
- Candidatura/desistencia de vagas;
- Atualizar perfil e experiências.

# Como executar o projeto em ambiente local

### Pré-requisitos: 
- [Python3](https://www.python.org/downloads/)
- [Postgresql](https://www.postgresql.org/download/)

```bash
#Se preferir, para instalar os pacotes abaixo, execute:

pip install -r requirements.txt
```

- [Django4](https://www.djangoproject.com/download/)
- [Random Username Generator](https://pypi.org/project/random-username/)
- [Psycopg2](https://pypi.org/project/psycopg2/)

### Instalação
```bash
# clonar repositório
git clone https://github.com/NiRovil/Teste-PythonDjango
```

### Configuração

Após a clonar o repositório, você precisará configurar as opções de database no arquivo setup/settings.py

```bash
[...]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<nome da sua database>',
        'USER': '<nome de usuario da sua database>',
        'PASSWORD': '<senha da sua database>',
        'HOST': 'localhost'
    }
}

```

### Iniciando a aplicação

```bash
# executar a migração do banco de dados
python manage.py makemigrations
python manage.py migrate

# executar o projeto
python manage.py runserver
```

Para visualizar o conteúdo da aplicação basta acessar
- localhost:8000

# Como executar o projeto em ambiente Docker

### Pré-requisitos

Para rodar esse container você precisa do docker instalado em sua máquina.

- [Windows](https://docs.docker.com/desktop/install/windows-install/)
- [OS X](https://docs.docker.com/desktop/install/mac-install/)
- [Linux](https://docs.docker.com/desktop/install/linux-install/)

## Preparando o ambiente docker

Abaixo algumas configurações para a inicialização do ambiente docker.

#### Atentar-se que os arquivos a seguir precisam estar no mesmo diretorio do projeto!

### Dockerfile

#### Variáveis de ambiente

`WORKDIR` > Diretorio onde está localizado o projeto

##### Dockerfile

```bash
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR ../Teste-PythonDjango

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/
```

### Docker Compose

#### Variáveis de ambiente

- `POSTGRES_NAME` > Nome da database
- `POSTGRES_DB` > Nome da database
- `POSTGRES_USER` > Nome do usuário da database
- `POSTGRES_PASSWORD` > Senha para acesso a database

##### docker-compose.yml

```bash
version: "3.9"
   
services:
  db:
    image: postgres:latest
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=...
      - POSTGRES_USER=...
      - POSTGRES_PASSWORD=...
  web:
    build: .
    command: bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    environment:
      - POSTGRES_NAME=...
      - POSTGRES_USER=...
      - POSTGRES_PASSWORD=...
    depends_on:
      - db
```
```bash
# Caso queira uma versão interativa com o banco de dados, anexar o código abaixo ao docker-compose.yml:

  pgadmin:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: ...
      PGADMIN_DEFAULT_PASSWORD: ...
    ports:
      - "16543:80"
    depends_on:
      - db
```

## Configuração

Antes de iniciar o container, você precisará configurar as opções de database no arquivo setup/settings.py

```bash
[...]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db'
        'PORT': 5432,
    }
}
```

## Iniciando a aplicação

```bash
# executar os containeres
docker-compose up
```

Para visualizar o conteúdo da aplicação basta acessar
- localhost:8000

Para visualizar o conteúdo do banco de dados basta acessar
- localhost:16543


# Autor

Nicolas Robert Vilela

### Onde me encontrar

https://www.linkedin.com/in/nicolas-robert-vilela-251318182/
