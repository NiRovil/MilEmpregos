# MilEmpregos 
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/NiRovil/MilEmpregos/blob/main/LICENSE) 

### Sobre o projeto

O projeto MilEmpregos é uma aplicação web, construída em Python, usando o framework Django.

A aplicação consiste na criação e divulgação de vagas de emprego, tal qual, a inscrição de candidatos nessas vagas.

# Tecnologias utilizadas
### Back end
- Python
- Django
### Front end
- HTML / CSS - templates by: [colorlib.com](https://colorlib.com/)

# Recursos

- Cadastrar usuários (candidatos e empresas);
- Autenticação e login;
- Cadastrar/deletar vagas;
- Candidatura/desistencia de vagas;
- Atualizar perfil e experiências.

# Demonstração

### Index

![alt text](https://github.com/NiRovil/MilEmpregos/blob/main/media/fotos/Pagina%20Inicial%20s%20Sidebar.png)

### Dashboard candidatos

![alt text](https://github.com/NiRovil/MilEmpregos/blob/main/media/fotos/Dashboard%20candidato.png)

### Dashboard empresas

![alt text](https://github.com/NiRovil/MilEmpregos/blob/main/media/fotos/Dashboard%20empresas.png)

#### Mais conteúdo em

[Imagens do projeto](https://github.com/NiRovil/MilEmpregos/tree/main/media/fotos)

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
git clone https://github.com/NiRovil/MilEmpregos
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

### Instalação
```bash
# clonar repositório
git clone https://github.com/NiRovil/MilEmpregos
```

#### Atentar-se que os arquivos a seguir precisam estar no mesmo diretorio do projeto!

### Dockerfile

##### Dockerfile

```bash
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/
```

### Docker Compose

##### docker-compose.yml

```bash
version: "3.9"
   
services:
  db:
    image: postgres:latest
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
  web:
    build: .
    command: bash -c "python /code/manage.py makemigrations && python /code/manage.py migrate && python /code/manage.py runserver 0.0.0.0:8000"
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    environment:
      - POSTGRES_NAME=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
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
        'HOST': 'db',
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

# Autor

Nicolas Robert Vilela

### Onde me encontrar

https://www.linkedin.com/in/nicolas-robert-vilela-251318182/
