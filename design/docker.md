# Documentação de Containerização com Docker 

## 1. Visão Geral 

Este documento descreve o processo de containerização do microserviço usando Docker. O objetivo é garantir que a aplicação seja facilmente empacotada e executável em qualquer ambiente compatível com containers.

---

## 2. Dockerfile

Abaixo está o `Dockerfile` utilizado no projeto:

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

## 3. Explicação por etapas

| Etapa | Descrição |
|-------|-----------|
| FROM python:3.11-slim | Define a imagem base como a versão slim da imagem oficial do Python. |
| WORKDIR /app | Define o diretório de trabalho para /app. |
| COPY requirements.txt . | Copia o arquivo requirements.txt para o diretório de trabalho. |
| RUN pip install --no-cache-dir -r requirements.txt | Instala as dependências do projeto. |
| COPY . . | Copia o código do projeto para o diretório de trabalho. |
| EXPOSE 8000 | Exponha a porta 8000 para o host. |
| CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] | Define o comando de inicialização da aplicação. |

## 4. Como executar o container

### 4.1. Criar a imagem

```bash
docker build -t microservice-api .
```

### 4.2. Executar o container

```bash
docker run -d -p 8000:8000 microservice-api
``` 
Acesse a API em: http://localhost:8000

## 5. Requisitos

- Ter o Docker instalado.
- Ter o arquivo requirements.txt na raiz do projeto.
- Ter o arquivo main.py na raiz do projeto.

## 6. Melhorias

- Suporte a variáveis de ambiente com python-dotenv
- Adicionar suporte a Docker Compose para banco de dados
- Utilizar multistage build para otimização de imagem
