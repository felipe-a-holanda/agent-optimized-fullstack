{% raw %}
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register(client: AsyncClient):
    response = await client.post(
        "/api/auth/register",
        json={
            "email": "new@example.com",
            "password": "securepassword",
            "full_name": "New User",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "new@example.com"
    assert "hashed_password" not in data


@pytest.mark.asyncio
async def test_register_duplicate_email(client: AsyncClient, test_user):
    response = await client.post(
        "/api/auth/register",
        json={"email": "test@example.com", "password": "another"},
    )
    assert response.status_code == 409


@pytest.mark.asyncio
async def test_login(client: AsyncClient, test_user):
    response = await client.post(
        "/api/auth/login",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "access_token" in response.cookies


@pytest.mark.asyncio
async def test_login_wrong_password(client: AsyncClient, test_user):
    response = await client.post(
        "/api/auth/login",
        json={"email": "test@example.com", "password": "wrong"},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_me(authenticated_client: AsyncClient):
    response = await authenticated_client.get("/api/auth/me")
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"


@pytest.mark.asyncio
async def test_get_me_unauthenticated(client: AsyncClient):
    response = await client.get("/api/auth/me")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_logout(authenticated_client: AsyncClient):
    response = await authenticated_client.post("/api/auth/logout")
    assert response.status_code == 200
{% endraw %}
