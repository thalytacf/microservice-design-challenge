# Design da API

Este documento descreve o design da API REST do microsserviço, abordando os endpoints disponíveis, validações de entrada, exemplos de payload e requisitos de desempenho.

## Objetivo do Microsserviço

Criar um microsserviço escalável e de fácil manutenção que receba e armazene grandes volumes de dados, com validação rigorosa das entradas e acesso eficiente às informações persistidas.

---

## Endpoints

### POST `/data`

Recebe um payload JSON, valida os dados e os persiste no banco de dados.

* **Request Body:**

```json
{
  "id": 1,
  "name": "example",
  "value": 123.45
}
```

* **Validações:**

  * `id`: obrigatório, inteiro
  * `name`: obrigatório, string
  * `value`: obrigatório, número decimal

* **Respostas:**

  * `201 Created`: item criado com sucesso
  * `422 Unprocessable Entity`: payload inválido

---

### GET `/data`

Retorna todos os dados armazenados.

* **Resposta:**

```json
[
  {
    "id": 1,
    "name": "example",
    "value": 123.45
  },
  {
    "id": 2,
    "name": "another",
    "value": 678.90
  }
]
```

* **Status code:**

  * `200 OK`: sucesso

---

## Considerações de Desempenho

* Os endpoints devem responder em até **500ms** sob carga normal.
* A arquitetura suporta **milhões de registros**, com no máximo **10% de degradação** no tempo de resposta.
* Uso de banco de dados com suporte a índices para acelerar leituras.

---

## Observações

* A API segue o padrão REST.
* Todas as entradas são validadas com base em modelos Pydantic.
* A escalabilidade horizontal permite atender a muitos usuários simultâneos.
