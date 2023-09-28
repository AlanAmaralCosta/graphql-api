# GraphQL API

Este projeto faz parte da Disciplina **Desenvolvimento Full Stack Avançado** 

O objetivo é uma API GraphQL que se conecta com um banco de dados Postgres que está em um container que será executado juntamente com esse projeto através do compose este projeto implementa uma interface completa para uso do banco de dados Postgres para gravar DVDs e recuperar, alterar, deletar e incluir, bem como consultar inclusive com algus filtros.

As principais tecnologias que serão utilizadas aqui é o:
 - [FastAPI](https://fastapi.tiangolo.com/)
 - [Postgres](https://www.postgresql.org/)
 - [Docker](https://www.docker.com/)
 - [Strawberry](https://strawberry.rocks/)
 - [GraphQL](https://graphql.org/)

---
### Instalação


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

---
### Executando o servidor


Para executar a API vamos usar o compose então seguem as instruções

```
(env)$ docker compose up --build
```

Isso irá gerar os containers e as dependias dele para que a API funcione corretamente.

```
### Acesso no browser

Abra o [http://0.0.0.0:8001](http://0.0.0.0:8001) no navegador para verificar o status da conexão com o banco de dados.

Abra o [http://0.0.0.0:8001/graphql](http://0.0.0.0:8001/graphql) no navegador para acessar a rota do graphQl

---
### Alguns comandos úteis do Docker

Em nosso caso específico é bom sempre usar nessa ordem, se precisar parar a execução:
docker compose down

docker compose down -v

___

### Comandos uteis de GraphQL

# Criar um DVD

mutation {
  createDvd(
    title: "Meu DVD de Teste",
    director: "Diretor de Teste",
    releaseYear: 2023,
    genre: "Ação"
  ) {
    id
    title
    director
    releaseYear
    genre
  }
}

# Update por ID

mutation {
  updateDvd(
    id: 16,  # Substitua pelo ID do DVD que deseja atualizar
    title: "Meu DVD de Teste Updated",
    director: "Diretor de Teste Updated",
    releaseYear: 2024,
    genre: "Ação"
  ) {
    id
    title
    director
    releaseYear
    genre
  }
}

# Deletar por ID

mutation {
  deleteDvd(
    id: 10  # Substitua pelo ID do DVD que deseja excluir
  )
}

# Consultar todos

query {
  dvds {
    id
    title
    director
    releaseYear
    genre
  }
}

# Consultar por ID

query {
  dvdById(id: 11) {
    id
    title
    director
    releaseYear
    genre
  }
}

# Consultar por Titulo - inclui os simulares

query {
  dvdsByTitle(title: "DVD 1") {
    id
    title
    director
    releaseYear
    genre
  }
}