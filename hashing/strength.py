import math
import string

# A small list of common passwords to check against
COMMON_PASSWORDS = [
    "123456", "password", "123456789", "12345678", "12345",
    "qwerty", "abc123", "password1", "1234567", "letmein"
]

def check_password_strength(password: str) -> dict:
    """
    Check the strength of a password and return a dictionary with the results.
    """
    if not password:
        return {"strength": "Weak", "score": 0, "reason": "Password is empty."}

    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    # Check if the password is in the common password list
    if password.lower() in COMMON_PASSWORDS:
        return {"strength": "Weak", "score": 1, "reason": "Password is too common."}

    # Calculate the score based on the criteria
    score = sum([has_upper, has_lower, has_digit, has_special])

    # Basic strength levels
    if length < 8 or score < 3:
        return {"strength": "Weak", "score": score, "reason": "Password is too short or lacks variety."}
    elif length >= 12 and score == 4:
        return {"strength": "Strong", "score": score, "reason": "Password is strong."}
    else:
        return {"strength": "Moderate", "score": score, "reason": "Password could be stronger."}

def calculate_entropy(password: str) -> float:
    """
    Calculate the entropy of a password based on character variety and length.
    """
    if not password:
        return 0.0

    length = len(password)  # Fix: Added length calculation here

    charset_size = 0
    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char.isdigit() for char in password):
        charset_size += 10
    if any(char in string.punctuation for char in password):
        charset_size += len(string.punctuation)

    # Entropy calculation: log2(charset_size^length)
    entropy = length * math.log2(charset_size) if charset_size > 0 else 0.0
    return round(entropy, 2)

# Example Usage
if __name__ == "__main__":
    test_password = "SecureP@ss123"
    strength_result = check_password_strength(test_password)
    entropy_value = calculate_entropy(test_password)

    print(f"Password Strength: {strength_result}")
    print(f"Password Entropy: {entropy_value} bits")
