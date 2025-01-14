import pytest
from hashing.hasher import bcrypt_hash, bcrypt_verify, argon2_hash, argon2_verify

# Test data
TEST_PASSWORD = "SecureP@ss123"
INVALID_PASSWORD = "WrongPassword"

# Test bcrypt_hash
def test_bcrypt_hash():
    hashed_password = bcrypt_hash(TEST_PASSWORD)
    assert hashed_password.startswith("$2b$"), "Bcrypt hash should start with $2b$"
    assert bcrypt_verify(TEST_PASSWORD, hashed_password) is True, "Bcrypt verification should return True for correct password"
    assert bcrypt_verify(INVALID_PASSWORD, hashed_password) is False, "Bcrypt verification should return False for incorrect password"

# Test argon2_hash
def test_argon2_hash():
    hashed_password = argon2_hash(TEST_PASSWORD)
    assert hashed_password.startswith("$argon2id$"), "Argon2 hash should start with $argon2id$"
    assert argon2_verify(TEST_PASSWORD, hashed_password) is True, "Argon2 verification should return True for correct password"
    assert argon2_verify(INVALID_PASSWORD, hashed_password) is False, "Argon2 verification should return False for incorrect password"

