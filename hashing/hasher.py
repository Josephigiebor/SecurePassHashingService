import bcrypt
from argon2 import PasswordHasher, exceptions as argon_exceptions

# Argon2 Hasher Instance
argon2_hasher = PasswordHasher()

# Bcrypt Hashing Functions
def bcrypt_hash(password: str) -> str:
    """
    Hash a password using bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def bcrypt_verify(password: str, hashed: str) -> bool:
    """
    Verify a password against a bcrypt hash.
    """
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    except ValueError:
        return False

# Argon2 Hashing Functions
def argon2_hash(password: str) -> str:
    """
    Hash a password using Argon2.
    """
    return argon2_hasher.hash(password)

def argon2_verify(password: str, hashed: str) -> bool:
    """
    Verify a password against an Argon2 hash.
    """
    try:
        return argon2_hasher.verify(hashed, password)
    except argon_exceptions.VerifyMismatchError:
        return False
    except argon_exceptions.VerificationError:
        return False
    except argon_exceptions.InvalidHash:
        return False

# Example Usage
if __name__ == "__main__":
    # Example for bcrypt
    password = "SecureP@ss123"
    hashed_password_bcrypt = bcrypt_hash(password)
    print(f"Bcrypt Hashed Password: {hashed_password_bcrypt}")
    print(f"Verification: {bcrypt_verify(password, hashed_password_bcrypt)}")

    # Example for argon2
    hashed_password_argon2 = argon2_hash(password)
    print(f"Argon2 Hashed Password: {hashed_password_argon2}")
    print(f"Verification: {argon2_verify(password, hashed_password_argon2)}")
