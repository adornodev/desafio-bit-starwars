# Desafio StarWars

Trata-se de uma API que integra com o serviço público **[SWAPI][swapi]** para complementar informações a respeito dos planetas de StarWars.

A aplicação desenvolvida utiliza Flask como framework web e MongoDB como banco de dados para o armazenamento de informações pertinentes aos planetas. Ambas as tecnologias estão containerizadas.

<p align="center">
  <img src=".github/header.png">
</p>

## Dependências

Para rodar a aplicação, a máquina deve possuir as seguintes ferramentas:

- **[docker][docker]**
- **[docker-compose][docker-compose]**

## Como rodar?

Primeiramente deve clonar o repositório em seu computador:

```
https://github.com/adornodev/desafio-bit-starwars.git
```

Com o repositório clonado, na raiz principal do projeto há um arquivo chamado _requirements_txt_. Nele consta todas as dependências necessárias para a execução do projeto.

Para iniciar a aplicação junto ao banco de dados, execute o comando:

```docker
docker-compose up -d
```

Para interromper a execução, execute

```docker
docker-compose stop
```

Pronto, a **aplicação** está exposta localmente na **porta 5000**!

---

## Exemplos de uso

Caso tenha o **[Insomnia][insomnia]** instalado, clique no botão abaixo para carregar todos os exemplos possíveis de requests

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=BitSW&uri=https%3A%2F%2Fraw.githubusercontent.com%2Fadornodev%2Fdesafio-bit-starwars%2Fmaster%2F.github%2Finsomnia_workspace.json)

**Resource:** /planets

| Tipo de Request | Descrição                                                                                         | Route Params                              | Query Params                | Body de exemplo                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------- |
| DELETE          | Deleta um planeta da base de dados                                                                | id do planeta da SWAPI ou nome do planeta |                             |                                                                                               |
| POST            | Insere um planeta na base de dados. <br><br> Campos possíveis: **name**, **terrain**, **climate** |                                           |                             | <code>{"name":"Alderaan", "climate": "temperature","terrain": "grasslands, mountains"}</code> |
| GET             | Busca todos os planetas da base de dados                                                          |                                           | page, page_size (default 5) | Payload                                                                                       |
| GET             | Busca por um planeta em específico                                                                | id do planeta da SWAPI ou nome do planeta |                             |

[swapi]: https://swapi.co/
[insomnia]: https://insomnia.rest/
[docker]: https://www.docker.com/products/docker-desktop
[docker-compose]: https://docs.docker.com/compose/install/
