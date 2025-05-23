import pytest
from httpx import ASGITransport, AsyncClient

from main import app


@pytest.mark.asyncio
async def test_post_data_success():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "id": 1,
            "name": "example",
            "value": 123.45
        }
        response = await ac.post("/data", json=payload)
    
    assert response.status_code in [200, 201]
    assert "message" in response.json()
    assert response.json()["message"] == "Item criado com sucesso"

@pytest.mark.asyncio
async def test_post_data_invalid():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"wrong_field": 123}
        response = await ac.post("/data", json=payload)
    
    assert response.status_code == 422
    assert "detail" in response.json()  # Verificar a estrutura do erro
    assert "missing" in response.json()["detail"][0]["type"]

@pytest.mark.asyncio
async def test_post_data_missing_field():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {"id": 1}  # Faltando o campo 'name' e 'value'
        response = await ac.post("/data", json=payload)
    
    assert response.status_code == 422
    assert "detail" in response.json()
    assert "missing" in response.json()["detail"][0]["type"]

@pytest.mark.asyncio
@pytest.mark.parametrize("payload", [
    {},  # vazio
    {"id": "abc", "name": "x", "value": 10},  # id errado
    {"id": 1, "name": 123, "value": 10},  # name errado
    {"id": 1, "name": "ok", "value": "wrong"},  # value errado
    {"id": 1, "name": "ok", "value": 10, "extra": "unexpected"},  # extra
])
async def test_post_data_invalid_cases(payload):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/data", json=payload)

    assert response.status_code == 422
    assert "detail" in response.json()
