# Documentação de CI/CD com GitHub Actions

## Visão Geral

Este documento descreve o pipeline de CI/CD utilizado para o microserviço, implementado com **GitHub Actions**. O objetivo é automatizar as etapas de build da imagem Docker, push para o registro de containers e aplicação dos manifests no cluster Kubernetes.

---

## 1. Estrutura do Workflow

O arquivo de workflow está localizado em:
`.github/workflows/deploy.yaml`


O pipeline é acionado automaticamente em cada push na branch `main`.

---

## 2. Etapas do Pipeline

### 2.1 Checkout do código

```yaml
- name: Checkout código
  uses: actions/checkout@v3
```

Obtém o código-fonte do repositório para a máquina virtual do GitHub Actions.

### 2.2 Login no GitHub Container Registry

```yaml
- name: Login no GitHub Container Registry
  uses: docker/login-action@v2
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}
```

Autentica no registro de containers do GitHub.

### 2.3 Build da imagem Docker

```yaml
- name: Build da imagem Docker
  run: |
    docker build -t $REGISTRY/${IMAGE_NAME}:latest .
```
Cria a imagem Docker com a tag latest, utilizando o Dockerfile na raiz do projeto.

### 2.4 Push da imagem para o GHCR

```yaml
- name: Push da imagem para o GHCR
  run: |
    docker push $REGISTRY/${IMAGE_NAME}:latest
``` 

Envia a imagem para o registro de containers do GitHub, tornando-a disponível para o cluster Kubernetes.

### 2.5 Deploy no Kubernetes

```yaml
- name: Deploy no Kubernetes
  uses: azure/k8s-deploy@v4
  with:
    manifests: |
      kubernetes/deployment.yaml
      kubernetes/service.yaml
      kubernetes/configmap.yaml
      kubernetes/hpa.yaml
    images: |
      ghcr.io/${{ github.repository }}:latest
    namespace: default
    kubeconfig: ${{ secrets.KUBECONFIG }}
```

Aplica os manifests do Kubernetes no cluster.

---

## 3. Requisitos

- Configurar o segredo KUBECONFIG com acesso ao cluster.
- Configurar o repositório para permitir publicação no ghcr.io (GitHub Container Registry).
- Ter os manifests do Kubernetes prontos na pasta kubernetes/.

---

## 4. Melhorias

- Adicionar etapa de testes automatizados antes do build da imagem.
- Validar YAMLs com kubectl dry-run antes do apply.
- Notificações por Slack ou email em caso de falha.
- Deploy apenas após aprovação de Pull Requests (com GitHub Environments).

