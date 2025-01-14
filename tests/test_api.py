import requests

# Use your Heroku URL for remote testing
BASE_URL = "https://secure-pass-0b6641220537.herokuapp.com"

# Test for the /hash endpoint
def test_hash_password():
    response = requests.post(f"{BASE_URL}/hash", json={"password": "securepass123"})
    assert response.status_code == 200
    data = response.json()
    assert "bcrypt_hashed" in data
    assert "argon2_hashed" in data

# Test for the /verify endpoint
def test_verify_password():
    hash_response = requests.post(f"{BASE_URL}/hash", json={"password": "securepass123"})
    assert hash_response.status_code == 200
    hashed_password = hash_response.json()["bcrypt_hashed"]

    response = requests.post(f"{BASE_URL}/verify", json={
        "password": "securepass123",
        "hashed_password": hashed_password,
        "method": "bcrypt"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["is_valid"] is True

# Test for the /strength endpoint
def test_password_strength():
    response = requests.post(f"{BASE_URL}/strength", json={"password": "securepass123"})
    assert response.status_code == 200
    data = response.json()
    assert "score" in data
