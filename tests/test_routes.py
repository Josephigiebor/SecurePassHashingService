import pytest
from api.routes import app
from hashing.hasher import bcrypt_hash

@pytest.fixture
def client():
    """Flask test client fixture"""
    with app.test_client() as client:
        yield client

# Test the /verify endpoint
def test_verify_endpoint(client):
    password = "SecureP@ss123"
    bcrypt_hashed = bcrypt_hash(password)  # Generate bcrypt hash dynamically

    # Test valid password
    response = client.post('/verify', json={
        "password": password,
        "hashed_password": bcrypt_hashed,
        "method": "bcrypt"
    })
    data = response.get_json()

    assert response.status_code == 200, "Expected status code 200"
    assert data["is_valid"] is True, "Expected is_valid to be True for correct password"

    # Test invalid password
    response = client.post('/verify', json={
        "password": "WrongPassword",
        "hashed_password": bcrypt_hashed,
        "method": "bcrypt"
    })
    data = response.get_json()

    assert response.status_code == 200, "Expected status code 200"
    assert data["is_valid"] is False, "Expected is_valid to be False for incorrect password"
