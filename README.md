# Pague.AI Backend

API em Python com FastAPI, SQLAlchemy e Alembic. Banco PostgreSQL em Docker.

## Requisitos

* Python 3.12+
* Docker
* Git

## Variáveis de ambiente

Crie um arquivo `.env` na raiz:

``` 
DB_USER=pagueai_admin_user
DB_PASSWORD=1234
DB_HOST=127.0.0.1
DB_PORT=55432
DB_NAME=pagueai_database
HASH_KEY=supersecretkey
```
## Banco de dados com Docker

Suba um Postgres recente mapeando a porta 55432 para evitar conflito local.

```bash
docker rm -f pagueai-postgres 2>/dev/null || true
docker volume rm pagueai_pg 2>/dev/null || true
docker run -d --name pagueai-postgres -p 55432:5432 \
  -e POSTGRES_USER=pagueai_admin_user \
  -e POSTGRES_PASSWORD=1234 \
  -e POSTGRES_DB=pagueai_database \
  -v pagueai_pg:/var/lib/postgresql \
  postgres:latest
```

Teste rápido:

```bash
docker exec -it pagueai-postgres psql -U pagueai_admin_user -d pagueai_database -c "select version();"
```

## Configuração do ambiente Python

Dentro da pasta do projeto:

```bash
python -m venv .venv
# Windows PowerShell
. .venv/Scripts/Activate.ps1
# Linux ou macOS
# source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

## Criação e update do banco de dados

Ainda dentro da pasta do projeto:

```bash
alembic upgrade head
```

## Executar a API

Execute a partir da raiz do repositório para que o `.env` seja carregado:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

A API ficará em `http://localhost:8000`.  
Swagger em `http://localhost:8000/docs`.