# Persistência de Dados

## Escolha da Tecnologia

O banco de dados escolhido foi o **MongoDB**, uma base de dados NoSQL orientada a documentos, ideal para armazenar estruturas em JSON e lidar com grandes volumes de dados com flexibilidade e performance.

### Justificativas:

- **Flexibilidade no esquema**: Permite armazenar diferentes formatos de dados sem migrações complexas.
- **Desempenho em larga escala**: Suporte a sharding nativo para distribuição horizontal de dados.
- **Compatibilidade com JSON**: Integração direta com estruturas utilizadas na API.
- **Escalabilidade horizontal**: Facilidade de crescimento conforme a demanda.
- **Suporte robusto a índices**: Permite otimizações para leitura e escrita.

---

## Estratégia de Persistência

- Cada entrada do endpoint `POST /data` será armazenada como um documento em uma coleção MongoDB.
- Os campos esperados são:
  - `id`: inteiro (chave única)
  - `name`: string
  - `value`: float

### Considerações:

- O campo `id` é indexado para melhorar a busca e prevenir duplicatas.
- Os dados são validados antes da persistência, garantindo consistência.

---

## Modelagem e Escalabilidade

- A estrutura de documentos JSON permite fácil replicação e particionamento.
- Com o aumento de volume, é possível distribuir dados em múltiplos shards.
- A replicação assíncrona garante alta disponibilidade e tolerância a falhas.

---

## Futuras Otimizações

- Introdução de **TTL Indexes** para expirar dados antigos automaticamente (caso necessário).
- Análise de uso para criação de índices compostos baseados em queries reais.
- Uso de cache (como Redis) para leituras frequentes.
