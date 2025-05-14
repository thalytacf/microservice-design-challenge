# Microservice Backend Challenge

This project implements a backend microservice capable of receiving, validating, and persisting JSON data via HTTP. It showcases modern backend practices using FastAPI, containerization with Docker, orchestration via Kubernetes, and automation with GitHub Actions.


## Overview

* **Language:** Python
* **Framework:** FastAPI
* **Database:** MongoDB (suggested)
* **Containerization:** Docker
* **Orchestration:** Kubernetes
* **CI/CD:** GitHub Actions
* **Python Version**: 3.11+


---

## Documentation Overview

- [API Design](design/api.md)
- [Architecture](design/architecture.md)
- [Database](design/database.md)
- [Docker](design/docker.md)
- [Kubernetes](design/kubernetes.md)
- [CI/CD Pipeline](design/ci-cd.md)
- [Testing Strategy](design/testing.md)


## Architecture

![Microservice Architecture](docs/microservice-architecture.png)


### Layered Responsibilities

* **API Layer**: Handles HTTP requests, input validation and returns standardized responses.
* **Service Layer**: Contains the business logic, decouples API from persistence.
* **Database Layer**: Manages data access. Supports swapping databases with minimal impact.

---

## CI/CD Pipeline

Automated pipeline using **GitHub Actions** ([`.github/workflows/deploy.yaml`](.github/workflows/deploy.yaml)):

1. Checking out source code
2. Logging into GitHub Container Registry (GHCR)
3. Building Docker image
4. Pushing image to GHCR
5. Deploying to Kubernetes (via `kubectl` and manifests)

![CI/CD Pipeline](docs/pipeline.png)

---

## Kubernetes Configuration

YAML manifests provided:

* `deployment.yaml`
* `service.yaml`
* `configmap.yaml`
* `hpa.yaml`

All located in the `/k8s` folder. Deployment configured for horizontal scaling using HPA.

---

## Docker

Dockerfile provided in the project root. Minimal FastAPI app with:

* `main.py`: defines `POST /data` and `GET /data` endpoints
* `requirements.txt`: FastAPI, Uvicorn

---

## Testing Strategy

This project includes initial unit tests and outlines a broader testing strategy to ensure API correctness and future scalability.

### ✅ Implemented Tests

* **API Tests**
  * Successful creation via `POST /data` using valid payload
  * Async test execution using `httpx` and `pytest-asyncio`

Tests are located in the [`/test`](./test/) directory and can be executed with:

```bash
pytest
```

Libraries to use:

* `pytest`
* `httpx`
* `pytest-asyncio`

---

## How to Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run API
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## Deployment

**Requirements**:
- Docker installed
- Kubernetes cluster (local or remote)
- Secrets configured:
  - `KUBECONFIG` (cluster access)
  - `GITHUB_TOKEN` (for GHCR push)

Kubernetes manifests are located in `/kubernetes/` and ready to be applied.

---

## Future Improvements

* Add authentication and rate-limiting
* Include observability stack (Prometheus + Grafana)
* Enable GitHub Environments for PR approvals
* Setup full test automation

---

## Cloud Cost Estimation 

TO DO

---

## Final Notes

This project simulates a production-ready microservice with best practices in API design, modular architecture, infrastructure as code, and CI/CD automation.
