# Docker Containerization Documentation

## 1. Overview

This document describes the containerization process for the microservice using Docker. The goal is to ensure that the application is easily packaged and executable in any container-compatible environment.

---

## 2. Dockerfile

Below is the `Dockerfile` used in the project:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 3. Explanation by steps

| Step | Description |
|------|-------------|
| FROM python:3.11-slim | Define the base image as the slim version of the official Python image. |
| WORKDIR /app | Set the working directory to /app. |
| COPY requirements.txt . | Copy the requirements.txt file to the working directory. |
| RUN pip install --no-cache-dir -r requirements.txt | Install the project dependencies. |
| COPY . . | Copy the project code to the working directory. |
| EXPOSE 8000 | Expose port 8000 to the host. |
| CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] | Define the command to start the application. |

---

## 4. How to run the container

### 4.1. Create the image

```bash
docker build -t microservice-api .
```

### 4.2. Run the container

```bash
docker run -d -p 8000:8000 microservice-api
``` 

Access the API at: http://localhost:8000

---

## 5. Requirements

- Docker installed
- requirements.txt file in the root of the project
- main.py file in the root of the project

---

## 6. Improvements

- Add environment variable support with python-dotenv
- Add Docker Compose support for database
- Use multistage build for image optimization
