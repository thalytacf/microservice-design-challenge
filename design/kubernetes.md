# Documentação de Deploy com Kubernetes

## Visão Geral

Este documento descreve a estratégia de deployment no Kubernetes para o microserviço desenvolvido neste projeto. Ele inclui os principais recursos utilizados, a justificativa para cada escolha e como esses recursos contribuem para a escalabilidade, manutenção e operação do sistema.

---

## 1. Conceitos de Kubernetes Utilizados

### 1.1 Pod

Um **Pod** é a menor unidade executável no Kubernetes. Cada pod encapsula um container (ou mais de um) que compartilham rede e armazenamento. Neste projeto, cada pod executa uma instância do microserviço.

### 1.2 Deployment

O **Deployment** gerencia o ciclo de vida dos pods, incluindo sua criação, atualização e recuperação automática. Configuramos o deployment para manter **2 réplicas** do microserviço, garantindo alta disponibilidade e escalabilidade horizontal.

### 1.3 Service (ClusterIP)

Um **Service** é uma abstração que expõe a aplicação executada nos pods. Utilizamos um `ClusterIP`, que torna o serviço acessível apenas dentro do cluster — ideal para comunicação interna entre serviços.

### 1.4 ConfigMap

O **ConfigMap** armazena variáveis de ambiente e outras configurações em pares chave-valor, separadas do código da aplicação. Isso permite atualizar configurações sem a necessidade de reconstruir a imagem do container. Neste projeto, configuramos variáveis como `DATABASE_URL` e `ENVIRONMENT`.

### 1.5 Horizontal Pod Autoscaler (HPA)

O **HPA** ajusta automaticamente o número de pods com base no uso de CPU. Neste projeto, o deployment pode escalar de **2 até 5 pods** quando a utilização média de CPU ultrapassar **60%**, permitindo lidar com variações de carga sem intervenção manual.

---

## 2. Estrutura de Arquivos

Todos os manifestos do Kubernetes estão localizados no diretório `kubernetes/`:

| Arquivo             | Finalidade                                 |
|---------------------|---------------------------------------------|
| `deployment.yaml`   | Define o template do pod e o número de réplicas |
| `service.yaml`      | Expõe o deployment internamente via ClusterIP |
| `configmap.yaml`    | Declara variáveis de ambiente               |
| `hpa.yaml`          | Configura o autoescalonamento por CPU       |

---

## 3. Considerações de Escalabilidade

- **Aplicação stateless**: O microserviço não guarda estado, facilitando o escalonamento horizontal.
- **Deployment + HPA**: Permite escalar dinamicamente de acordo com a carga.
- **Abstração via Service**: Desacopla o acesso dos IPs dos pods, que mudam frequentemente.
- **Configuração via ConfigMap**: Permite adaptar variáveis por ambiente (ex: desenvolvimento, produção).

---

## 4. Melhorias Futuras

- Utilizar `Secrets` para variáveis sensíveis como senhas de banco de dados.
- Adicionar `Liveness` e `Readiness probes` para melhorar a resiliência.
- Integrar com um **Ingress Controller** para expor o serviço externamente via domínio.
- Monitorar métricas com ferramentas como Prometheus e Grafana.

---

## 5. Instruções de Deploy

Para aplicar os recursos:

```bash
kubectl apply -f kubernetes/

Para verificar o status:

```bash
kubectl get pods
kubectl get services
kubectl get hpa
