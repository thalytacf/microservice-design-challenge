# Kubernetes Deployment Documentation

## Overview

This document outlines the Kubernetes deployment strategy for the microservice developed in this project. It includes the key Kubernetes resources used, the rationale behind each choice, and how they contribute to the scalability, maintainability, and operability of the system.

---

## 1. Kubernetes Concepts Used

### 1.1 Pod

A Pod is the smallest deployable unit in Kubernetes. Each pod encapsulates a container (or multiple containers) that share network and storage. In this project, each pod runs one instance of the microservice container.

### 1.2 Deployment

The Deployment manages the lifecycle of pods, including their creation, update, and self-healing. We configured the deployment to maintain **2 replicas** of the microservice for high availability and scalability.

### 1.3 Service (ClusterIP)

A Service is an abstraction layer that exposes the application running in pods. We use a `ClusterIP` service, which makes the application accessible internally within the cluster, allowing communication between components without exposing it externally.

### 1.4 ConfigMap

The ConfigMap stores environment variables and other configuration values separately from the application code. This allows us to manage configuration without needing to rebuild container images. For example, `DATABASE_URL` and `ENVIRONMENT` are defined in the `ConfigMap` and injected into the container.

### 1.5 Horizontal Pod Autoscaler (HPA)

The HPA automatically scales the number of pods based on CPU usage. In our case, the deployment can scale from **2 to 5 pods** if the average CPU utilization exceeds **60%**. This ensures the system can handle increased load without manual intervention.

---

## 2. Files and Structure

All Kubernetes manifests are located in the `kubernetes/` directory:

| File             | Purpose                            |
|------------------|------------------------------------|
| `deployment.yaml`| Defines pod template and replicas  |
| `service.yaml`   | Exposes the deployment via ClusterIP |
| `configmap.yaml` | Declares environment variables     |
| `hpa.yaml`       | Configures auto-scaling based on CPU |

---

## 3. Scalability Considerations

- **Stateless application**: The microservice is stateless, making it easy to scale horizontally.
- **Deployment + HPA**: Enables dynamic scaling based on workload.
- **Service abstraction**: Decouples access from pod IPs, which change frequently.
- **Environment configuration**: `ConfigMap` ensures configurations can change per environment (e.g., dev, prod) without changing the image.

---

## 4. Future Improvements

- Use `Secrets` for sensitive environment variables like database passwords.
- Monitor metrics with Prometheus + Grafana or similar tools.

---

## 5. Deployment Instructions

To apply the resources, run:

```bash
kubectl apply -f kubernetes/
