# Estratégia de Testes

## Objetivo 

Esta seção descreve a abordagem planejada para testar o microserviço, com foco em garantir a **confiabilidade**, **validação de dados** e **comportamento esperado das APIs**. A estratégia cobre testes unitários, planos futuros de testes de integração e performance, além de ferramentas recomendadas para automação.

## Tipos de Testes

### 1. Testes Unitários / Unit Tests

- Validação de entrada de dados JSON (ex: campos obrigatórios, tipos corretos).
- Testes de funções isoladas, como persistência e leitura da base de dados simulada (mock).
- Verificação de retorno de erros esperados para entradas inválidas.

> **Ferramentas sugeridas:** `pytest`, `unittest`, `fastapi.testclient`.

---

### 2. Testes de Integração (futuros) / Integration Tests (planned)

- Testar o microserviço de ponta a ponta com uma instância real do banco de dados (ex: PostgreSQL ou MongoDB).
- Garantir que os endpoints funcionam corretamente com dados reais.

> **Futuramente**, o uso de `docker-compose` pode facilitar a criação de ambientes de teste com dependências.

---

### 3. Testes de Performance (futuros) / Performance Testing (planned)

- Validar o tempo de resposta das APIs, garantindo o limite de 500ms.
- Testar o sistema com grandes volumes de dados simulados.

> **Ferramentas sugeridas:** `Locust`, `Apache JMeter`, ou scripts com `httpx`.

---
## Cobertura Esperada

- Todas as **funções críticas** devem ser cobertas por testes.
- Validação completa de dados de entrada.
- Verificação de respostas esperadas em rotas principais (`POST /data`, `GET /data`).

> Meta inicial: **mínimo de 80% de cobertura nas rotas críticas.**

---

## Ferramentas Recomendadas

| Ferramenta | Descrição |
|------------|-----------|
| `pytest` | Framework de testes moderno e simples para Python. |
| `fastapi.testclient` | Cliente HTTP de testes para APIs FastAPI. |
| `coverage.py` | Ferramenta para medir cobertura de testes. |

---

## Melhorias Futuras 

- **Ambiente isolado:** Testes automatizados com banco de dados isolado via Docker.
- **Monitoramento:** Adição de testes contínuos de performance e alertas em produção.
