# CI/CD Documentation with GitHub Actions

## Overview

This document describes the CI/CD pipeline used for the microservice, implemented with **GitHub Actions**. The goal is to automate the steps of building the Docker image, pushing it to the container registry, and applying the Kubernetes manifests to the cluster.

---

## 1. Workflow Structure

The workflow file is located at:  
`.github/workflows/deploy.yaml`

The pipeline is automatically triggered on every push to the `main` branch.

---

## 2. Pipeline Steps

### 2.1 Checkout the code

```yaml
- name: Checkout code
  uses: actions/checkout@v3
```

This step retrieves the code from the repository and makes it available for the subsequent steps.

### 2.2 Login to GitHub Container Registry

```yaml
- name: Login to GitHub Container Registry
  uses: docker/login-action@v2
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}
```

This step authenticates to the GitHub Container Registry using the GitHub token.

### 2.3 Build the Docker image

```yaml
- name: Build the Docker image
  run: |
    docker build -t $REGISTRY/${IMAGE_NAME}:latest .
```

This step builds the Docker image with the latest tag, using the Dockerfile in the root of the project.

### 2.4 Push the image to the GHCR

```yaml
- name: Push image to GHCR
  run: |
    docker push $REGISTRY/${IMAGE_NAME}:latest
```

This step pushes the Docker image to the GitHub Container Registry.

### 2.5 Deploy to Kubernetes

```yaml
- name: Deploy to Kubernetes
  uses: azure/k8s-deploy@v4
  with:
    manifests: |
      kubernetes/deployment.yaml
    images: |
      ghcr.io/${{ github.repository }}:latest
    namespace: default
    kubeconfig: ${{ secrets.KUBECONFIG }}
```

This step applies the Kubernetes manifests to the cluster.

---

## 3. Requirements

- Configure the KUBECONFIG secret with access to the cluster.
- Configure the repository to allow publishing to ghcr.io (GitHub Container Registry).
- Have the Kubernetes manifests ready in the kubernetes/ directory.

---

## 4. Improvements

- Add automated tests before building the image.
- Validate YAMLs with kubectl dry-run before applying.
- Send Slack or email notifications on failure.
- Deploy only after Pull Request approval (using GitHub Environments).